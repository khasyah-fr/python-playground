
# Calculate theoretical maximized profit using marginal revenue and marginal cost

print(f"LOW Demand")
TR_low = float(input("Enter total revenue: "))
TC_low = float(input("Enter total cost: "))
Q_low = float(input("Enter quantity sold: "))

print(f"NORMAL Demand")
TR_normal = float(input("Enter total revenue: "))
TC_normal = float(input("Enter total cost: "))
Q_normal = float(input("Enter quantity sold: "))

print(f"HIGH Demand")
TR_high = float(input("Enter total revenue: "))
TC_high = float(input("Enter total cost: "))
Q_high = float(input("Enter quantity sold: "))

# Count marginal revenue and marginal cost
MR_1 = (TR_normal - TR_low) / (Q_normal - Q_low)
MR_2 = (TR_high - TR_normal) / (Q_high - Q_normal)

MC_1 = (TC_normal - TC_low) / (Q_normal - Q_low)
MC_2 = (TC_high - TC_normal) / (Q_high - Q_normal)

# Estimate the price where MR = MC
if abs(MR_1 - MC_1) < abs(MR_2 - MC_2):
    best_price = (TR_normal - TR_low) / (Q_normal - Q_low)
else:
    best_price = (TR_high - TR_normal) / (Q_high - Q_normal)

print(f"Best price is {best_price}")
print(f"MR1 {MR_1} MC1 {MC_1} MR2 {MR_2} MC2 {MC_2}")
print(f"Ratio1 {abs(MR_1 - MC_1)} Ratio2 {abs(MR_2 - MC_2)}")