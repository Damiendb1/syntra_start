# # beginnen met een zeer eenvoudige functie
# # even:
# #   domein: alle gehele getallen:
# #   bereik: bool
#
# def pos_neg_label(val: float) -> str:
#     """
#     Print negative of positive label for any number.
#     :param val: Number to check
#     :return: String label
#     """
#     if val < 0:
#         return "Negative"
#     if val > 0:
#         return "Positive"
#     return "Zero"
#
#
# # if pos_neg_label(-1.0) != "Negative":
# #     print("Error")
# # if pos_neg_label(1.0) != "Positive":
# #     print("Error")
# # if pos_neg_label(0.0) != "Zero":
# #     print("Error")
#
#
# expected = [(-1.0, "Negative"),
#             (1.0,"Positive"),
#             (0,"Zero")]
#
# for val, res in expected:
#     real_res = pos_neg_label(val)
#     if real_res != res:
#         print(f"Error:  {val} geeft {real_res}, ipv {res}")
#
#
#
# even = lambda x: x % 2 == 0
#
# results = set()
# for i in range(-400, 401, 1):
#     res = even(i)
#     print(i, even(i))
#     results.add(res)
# print("Moet True, False zijn", results)
#
#
# # equals = lambda x, y: x == y
#
# results = []
# for i in range(-400, 401, 1):
#     for j in range(-400, 401, 1):
#         res = equals(i,j)
#         if (i ==  j) != res:
#             print("ERROR")
#         if res not in results:
#             results.append(res)
# print("Moet True, False zijn", results)


def trouser_size(size: float):
    """
    Prints the name of a trouser size.
    :param size: Size of the trouser
    """
    if not 20 <= size <= 120:
        return None
        #return "geen correcte grootte ingegeven"
        #raise ValueError("Geen correct grootte")

    if size < 40:
        return "Small"
    if size < 50:
        return "Medium"
    if size < 60:
        return "Large"
    if size < 70:
        return "XL"
    return "XXL"
#
# results = []
# tests = [ -1.0, 39.0, 40.0, 45.0, 50.0, 55.0, 60.0, 65.0,  70.0, 75.0 ]
# for test in tests:
#     res =trouser_size(test)
#     if res is None:
#         print(f"grootte {test} is niet aanvaard")
#
# print("Moet Small,Medium ,Large, XL, XXL zijn", results)
#

# opdracht 1: schrijf code die test of trouser_size voor elke input de juiste output geeft.
#             beveilig de code tegen waardes die niet tussen 20 en 120 vallen.
expected = [(-1.0, None),
            (1.0,None),
            (19.9, None),
            (20.0, "Small"),
            (25.0, "Small"),
            (39.9, "Small"),
            (40.1, "Medium"),
            (49.9, "Medium"),
            (50, "Large"),
            (59.9, "Large"),
            (60.0, "XL"),
            (65.0, "XL"),
            (69.9, "XL"),
            (70, "XXL"),
            (80.0, "XXL"),
            (120, "XXL"),
            (121, None), ]

for val, res in expected:
    real_res = trouser_size(val)
    if real_res != res:
        print(f"Error:  {val} geeft {real_res}, ipv {res}")