class Gecko:
	def __init__(self, arm_len, leg_len, eyes, tail, furry):
		self.arm_length = float(arm_len)
		self.leg_length = float(leg_len)
		self.num_eyes = int(eyes)
		self.has_tail = bool(tail)
		self.is_furry = bool(furry)

	def describe_gecko(self):
		tail_str = "does" if self.has_tail else "does not"
		furry_str = "is" if self.is_furry else "is not"

		print("--- Gecko Characteristics ---")
		print(f"Arm Length: {self.arm_length} cm")
		print(f"Leg Length: {self.leg_length} cm")
		print(f"Number of Eyes: {self.num_eyes}")
		print(f"Tail: This animal {tail_str} have a tail.")
		print(f"Furry: This animal {furry_str} furry.")

my_gecko = Gecko(arm_len=4.8, leg_len=5.2, eyes=2, tail=True, furry=False)

my_gecko.describe_gecko()