"""
Citytrip Compare + Scoring + Scenario Grid (27 Nov 2025 → 1 Dec 2025)
---------------------------------------------------------------------
Wat dit script doet:
1) Vergelijkt steden op totale kost, bruikbare uren en € per bruikbare uur.
2) Weegt Kerstmarktscore + Weerfactor mee in een Overall Score.
3) Exporteert CSV’s + maakt 4 grafieken.
4) Draait een scenario-grid: verschillende voorkeur-gewichten → winnaar per scenario.

Gebruik:
- Pas onderaan FLIGHTS/BUDGETS + (optioneel) KERSTMARKT_SCORE/WEER_FACTOR/WEIGHTS aan.
- Run dit bestand. Alle Prive damien komt in ./Prive damien
Benodigdheden: pip install pandas matplotlib
"""

from __future__ import annotations
from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import Dict, List, Optional
from itertools import product
import math
import os

import pandas as pd
import matplotlib.pyplot as plt

# =============== Trip-instellingen ===============
TRIP_START = datetime(2025, 11, 27)
TRIP_END = datetime(2025, 12, 1)
NIGHTS = (TRIP_END - TRIP_START).days  # 4 nachten

# Aanpasbare aannames
SLEEP_HOURS_PER_NIGHT = 8.0
AIRPORT_TRANSFER_BUFFER_HOURS = 1.0    # 1u na aankomst + 1u voor terug (in de stad)
LOCAL_TRANSPORT_PER_DAY_DEFAULT = 6.0

# Wegingen (som ≈ 1) — pas naar smaak aan
WEIGHTS = {
    "cost": 0.5,
    "markets": 0.3,
    "weather": 0.2,
}

# Scenario-grid instellingen (kan je laten staan zoals is)
SCENARIOS_ENABLED = True
SCENARIO_COST = [0.2, 0.4, 0.6, 0.8]
SCENARIO_MARKETS = [0.0, 0.2, 0.4, 0.6]
SCENARIO_WEATHER = [0.0, 0.2, 0.4]


# =============== Dataclasses ===============
@dataclass
class FlightOption:
    price_eur: float
    depart: datetime         # vertrek (BRU/CRL lokale tijd)
    arrive: datetime         # aankomst (lokale tijd bestemming)
    return_depart: datetime  # vertrek terug (lokale tijd bestemming)
    return_arrive: datetime  # aankomst terug (lokale tijd home)
    depart_airport: str = "BRU"
    airline: Optional[str] = None

@dataclass
class CityBudget:
    lodging_per_night: float
    food_per_day: float
    local_transport_per_day: Optional[float] = None
    activities_per_day: float = 0.0
    airport_transfer_total: float = 0.0  # bv. retour metro/bus luchthaven ↔ centrum


# =============== Kernfuncties ===============
def compute_usable_hours(f: FlightOption) -> float:
    """Bruikbare tijd op bestemming (in uren)."""
    on_ground: timedelta = f.return_depart - f.arrive
    nights_on_ground = max(0, math.ceil(on_ground.total_seconds() / 86400))
    sleep_loss = nights_on_ground * SLEEP_HOURS_PER_NIGHT
    transfer_loss = 2 * AIRPORT_TRANSFER_BUFFER_HOURS
    usable = on_ground.total_seconds() / 3600 - sleep_loss - transfer_loss
    return max(0.0, usable)

def total_trip_cost(city: str, f: FlightOption, b: CityBudget) -> Dict[str, float]:
    days = (TRIP_END - TRIP_START).days
    local_transport = b.local_transport_per_day if b.local_transport_per_day is not None else LOCAL_TRANSPORT_PER_DAY_DEFAULT

    lodging_total = NIGHTS * b.lodging_per_night
    daily_total = days * (b.food_per_day + local_transport + b.activities_per_day)
    total = f.price_eur + lodging_total + daily_total + b.airport_transfer_total

    usable_hours = compute_usable_hours(f)
    cost_per_day = total / days if days else float("inf")
    cost_per_usable_hour = total / usable_hours if usable_hours > 0 else float("inf")

    return {
        "City": city,
        "Flight Price (€)": round(f.price_eur, 2),
        "Lodging Total (€)": round(lodging_total, 2),
        "Daily Spend Total (€)": round(daily_total, 2),
        "Airport Transfers (€)": round(b.airport_transfer_total, 2),
        "Total Trip Cost (€)": round(total, 2),
        "Usable Hours": round(usable_hours, 1),
        "Cost / Day (€)": round(cost_per_day, 2),
        "Cost / Usable Hour (€)": round(cost_per_usable_hour, 2),
        "Depart Airport": f.depart_airport,
        "Outbound": f"{f.depart.strftime('%a %d %b %H:%M')} → {f.arrive.strftime('%a %d %b %H:%M')}",
        "Return": f"{f.return_depart.strftime('%a %d %b %H:%M')} → {f.return_arrive.strftime('%a %d %b %H:%M')}",
        "Airline": f.airline or "-",
    }

def minmax(series: pd.Series) -> pd.Series:
    s = series.astype(float)
    mn, mx = s.min(), s.max()
    if mx == mn:
        return pd.Series([1.0] * len(s), index=s.index)
    return (s - mn) / (mx - mn)

def score_table(df: pd.DataFrame,
                kerst_scores: Dict[str, int],
                weer_scores: Dict[str, int]) -> pd.DataFrame:
    # Kosten → hogere score = goedkoper
    cost_norm_total = 1 - minmax(df["Total Trip Cost (€)"])
    cost_norm_cpu = 1 - minmax(df["Cost / Usable Hour (€)"])
    cost_score = 0.5 * cost_norm_total + 0.5 * cost_norm_cpu

    df = df.copy()
    df["Kerstmarktscore (0-10)"] = df["City"].map(kerst_scores).fillna(0).astype(float)
    df["Weerfactor (0-10)"] = df["City"].map(weer_scores).fillna(0).astype(float)
    market_score = df["Kerstmarktscore (0-10)"] / 10.0
    weather_score = df["Weerfactor (0-10)"] / 10.0

    overall = (
        WEIGHTS["cost"] * cost_score +
        WEIGHTS["markets"] * market_score +
        WEIGHTS["weather"] * weather_score
    )

    df["Cost Score (0-1, higher=better)"] = cost_score.round(3)
    df["Market Score (0-1)"] = market_score.round(3)
    df["Weather Score (0-1)"] = weather_score.round(3)
    df["Overall Score (0-1)"] = overall.round(3)

    cols = [
        "City",
        "Overall Score (0-1)",
        "Cost Score (0-1, higher=better)",
        "Market Score (0-1)",
        "Weather Score (0-1)",
        "Total Trip Cost (€)",
        "Cost / Usable Hour (€)",
        "Usable Hours",
        "Flight Price (€)",
        "Lodging Total (€)",
        "Daily Spend Total (€)",
        "Airport Transfers (€)",
        "Depart Airport",
        "Outbound",
        "Return",
        "Airline",
        "Kerstmarktscore (0-10)",
        "Weerfactor (0-10)",
    ]
    return df[cols].sort_values(by="Overall Score (0-1)", ascending=False).reset_index(drop=True)

def save_bar(x, y, title, ylabel, filename, outdir="Prive damien"):
    plt.figure()
    plt.bar(x, y)
    plt.title(title)
    plt.xlabel("City")
    plt.ylabel(ylabel)
    plt.xticks(rotation=30)
    plt.tight_layout()
    path = os.path.join(outdir, filename)
    plt.savefig(path, dpi=160)
    print(f"Saved: {path}")

# =============== Scenario-functies ===============
def normalize_weights(w: dict) -> dict:
    s = sum(w.values())
    return {k: (v / s if s else 0.0) for k, v in w.items()}

def compute_overall_with_weights(df_sorted: pd.DataFrame, weights: dict,
                                 kerst_scores: Dict[str, int],
                                 weer_scores: Dict[str, int]) -> pd.DataFrame:
    """Herbereken overall score met custom weights, return volledige scored table."""
    cost_norm_total = 1 - minmax(df_sorted["Total Trip Cost (€)"])
    cost_norm_cpu = 1 - minmax(df_sorted["Cost / Usable Hour (€)"])
    cost_score = 0.5 * cost_norm_total + 0.5 * cost_norm_cpu

    df = df_sorted.copy()
    df["Kerstmarktscore (0-10)"] = df["City"].map(kerst_scores).fillna(0).astype(float)
    df["Weerfactor (0-10)"] = df["City"].map(weer_scores).fillna(0).astype(float)
    market_score = df["Kerstmarktscore (0-10)"] / 10.0
    weather_score = df["Weerfactor (0-10)"] / 10.0

    w = normalize_weights(weights)
    overall = w["cost"] * cost_score + w["markets"] * market_score + w["weather"] * weather_score

    df["Cost Score (0-1, higher=better)"] = cost_score
    df["Market Score (0-1)"] = market_score
    df["Weather Score (0-1)"] = weather_score
    df["Overall Score (0-1)"] = overall
    return df.sort_values(by="Overall Score (0-1)", ascending=False).reset_index(drop=True)

def generate_weight_grid() -> List[dict]:
    scenarios = []
    for c, m, w in product(SCENARIO_COST, SCENARIO_MARKETS, SCENARIO_WEATHER):
        if c + m + w == 0:
            continue
        scenarios.append({"cost": c, "markets": m, "weather": w})
    return scenarios

def run_scenarios(df_sorted: pd.DataFrame,
                  kerst_scores: Dict[str, int],
                  weer_scores: Dict[str, int]) -> None:
    os.makedirs("", exist_ok=True)
    scenarios = generate_weight_grid()
    winner_rows, score_rows = [], []
    win_counts: Dict[str, int] = {}

    for i, weights in enumerate(scenarios, start=1):
        scored = compute_overall_with_weights(df_sorted, weights, kerst_scores, weer_scores)
        winner = scored.iloc[0]["City"]
        top2 = scored.iloc[1]["City"] if len(scored) > 1 else ""
        top3 = scored.iloc[2]["City"] if len(scored) > 2 else ""
        win_counts[winner] = win_counts.get(winner, 0) + 1

        wnorm = normalize_weights(weights)
        winner_rows.append({
            "Scenario": i,
            "Weights_cost": round(wnorm["cost"], 3),
            "Weights_markets": round(wnorm["markets"], 3),
            "Weights_weather": round(wnorm["weather"], 3),
            "Winner": winner,
            "2nd": top2,
            "3rd": top3
        })

        for _, r in scored.iterrows():
            score_rows.append({
                "Scenario": i,
                "City": r["City"],
                "Overall Score (0-1)": round(float(r["Overall Score (0-1)"]), 4)
            })

    winners_df = pd.DataFrame(winner_rows)
    winners_path = os.path.join("", "scenario_winners.csv")
    winners_df.to_csv(winners_path, index=False)

    scores_df = pd.DataFrame(score_rows)
    scores_path = os.path.join("", "scenario_scores.csv")
    scores_df.to_csv(scores_path, index=False)

    print(f"Scenario CSV saved:\n- {winners_path}\n- {scores_path}")

    if win_counts:
        cities = list(win_counts.keys())
        counts = [win_counts[c] for c in cities]
        plt.figure()
        plt.bar(cities, counts)
        plt.title("Scenario Wins per City")
        plt.xlabel("City")
        plt.ylabel("#Wins across scenarios")
        plt.xticks(rotation=30)
        plt.tight_layout()
        win_png = os.path.join("", "scenario_win_counts.png")
        plt.savefig(win_png, dpi=160)
        print(f"Saved: {win_png}")


# =============== Data (PAS HIER AAN) ===============
FLIGHTS: Dict[str, FlightOption] = {
    "Vienna":   FlightOption(120, datetime(2025,11,27,7,25), datetime(2025,11,27,9,10),
                             datetime(2025,11,30,20,30), datetime(2025,11,30,22,15), "BRU", "Austrian"),
    "Prague":   FlightOption(95, datetime(2025,11,27,8,50), datetime(2025,11,27,10,25),
                             datetime(2025,11,30,21,5), datetime(2025,11,30,22,40), "CRL", "Ryanair"),
    "Rome":     FlightOption(130, datetime(2025,11,27,6,55), datetime(2025,11,27,9,0),
                             datetime(2025,11,30,21,0), datetime(2025,11,30,23,10), "BRU", "Brussels Airlines"),
    "Warsaw":   FlightOption(110, datetime(2025,11,27,7,15), datetime(2025,11,27,9,20),
                             datetime(2025,11,30,20,45), datetime(2025,11,30,22,55), "BRU", "LOT"),
    "Tenerife": FlightOption(180, datetime(2025,11,27,7,0), datetime(2025,11,27,11,30),
                             datetime(2025,11,30,16,45), datetime(2025,11,30,22,45), "CRL", "Ryanair"),
    "Valencia": FlightOption(115, datetime(2025,11,27,7,10), datetime(2025,11,27,9,30),
                             datetime(2025,11,30,21,15), datetime(2025,11,30,23,45), "CRL", "Ryanair"),
    "Porto":    FlightOption(105, datetime(2025,11,27,7,0), datetime(2025,11,27,9,0),
                             datetime(2025,11,30,21,30), datetime(2025,11,30,23,55), "CRL", "Ryanair"),
}

BUDGETS: Dict[str, CityBudget] = {
    "Vienna":   CityBudget(48, 35, 6, 10, 12),
    "Prague":   CityBudget(28, 25, 5, 10, 8),
    "Rome":     CityBudget(55, 30, 6, 12, 14),
    "Warsaw":   CityBudget(35, 22, 5, 8, 10),
    "Tenerife": CityBudget(50, 28, 7, 12, 16),
    "Valencia": CityBudget(45, 28, 5, 10, 10),
    "Porto":    CityBudget(40, 27, 5, 10, 10),
}

KERSTMARKT_SCORE = {
    "Vienna": 10, "Prague": 9, "Rome": 4, "Warsaw": 6, "Tenerife": 1, "Valencia": 3, "Porto": 4
}
WEER_FACTOR = {
    "Vienna": 5, "Prague": 5, "Rome": 7, "Warsaw": 4, "Tenerife": 9, "Valencia": 8, "Porto": 7
}


# =============== Main ===============
def main() -> None:
    os.makedirs("", exist_ok=True)

    # 1) Basis vergelijking
    rows: List[Dict[str, float]] = []
    for city, flight in FLIGHTS.items():
        budget = BUDGETS.get(city)
        if budget is None:
            continue
        rows.append(total_trip_cost(city, flight, budget))

    df = pd.DataFrame(rows)
    df_sorted = df.sort_values(
        by=["Total Trip Cost (€)", "Cost / Usable Hour (€)"],
        ascending=[True, True]
    ).reset_index(drop=True)

    # 2) Scoring
    df_scored = score_table(df_sorted, KERSTMARKT_SCORE, WEER_FACTOR)

    # 3) CSV’s
    path_compare = os.path.join("", "trip_comparison_27Nov_1Dec.csv")
    path_scored = os.path.join("", "trip_scored_27Nov_1Dec.csv")
    df_sorted.to_csv(path_compare, index=False)
    df_scored.to_csv(path_scored, index=False)
    print(f"CSV saved:\n- {path_compare}\n- {path_scored}")

    # 4) Grafieken
    save_bar(df_sorted["City"], df_sorted["Total Trip Cost (€)"],
             "Total Trip Cost (€)", "€", "total_cost.png")
    save_bar(df_sorted["City"], df_sorted["Cost / Usable Hour (€)"],
             "Cost per Usable Hour (€)", "€ per hour", "cost_per_usable_hour.png")
    save_bar(df_sorted["City"], df_sorted["Usable Hours"],
             "Usable Hours on the Ground", "Hours", "usable_hours.png")
    save_bar(df_scored["City"], df_scored["Overall Score (0-1)"],
             "Overall City Score (higher is better)", "Score (0-1)", "overall_score.png")

    # 5) Scenario-grid (optioneel)
    if SCENARIOS_ENABLED:
        run_scenarios(df_sorted, KERSTMARKT_SCORE, WEER_FACTOR)

    print("Klaar! Pas data/gewichten aan en run opnieuw voor snelle what-if analyses.")

if __name__ == "__main__":
    main()
