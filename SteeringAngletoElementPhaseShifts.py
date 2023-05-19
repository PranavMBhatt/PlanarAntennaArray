import math

# inputs
M_max = int(input("Enter the maximum value for M: "))
N_max = int(input("Enter the maximum value for N: "))
SteeringAngleTheta = float(input("Enter the steering angle (theta) in degrees: "))
SteeringAnglePhi = float(input("Enter the steering angle (phi) in degrees: "))
dy = float(input("Enter the value for dy in meters: "))
dx = float(input("Enter the value for dx in meters: "))
frequency = float(input("Enter the frequency in Hz: "))
c = 3e8  # Speed of light

# deg to radians
SteeringAngleTheta_rad = math.radians(SteeringAngleTheta)
SteeringAnglePhi_rad = math.radians(SteeringAnglePhi)

# Scan phase shifts
ScanPhaseShiftY = -(frequency * 2 * math.pi * dy / c * math.sin(SteeringAngleTheta_rad) * math.sin(SteeringAnglePhi_rad))
ScanPhaseShiftX = -(frequency * 2 * math.pi * dx / c * math.sin(SteeringAngleTheta_rad) * math.cos(SteeringAnglePhi_rad))

# Element phase for each (M, N) combination
for M in range(1, M_max + 1):
    for N in range(1, N_max + 1):
        ElementMNPhase = math.degrees((M - 1) * ScanPhaseShiftY + (N - 1) * ScanPhaseShiftX) % 360
        print(f"Element{M}{N}Phase = {ElementMNPhase} degrees")
