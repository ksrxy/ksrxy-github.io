# main.py

from config import SIMULATION_TIME
from crypto_sim import CryptoSimulation

if __name__ == '__main__':
    print(f"Simulation Time: {SIMULATION_TIME} seconds")
    sim = CryptoSimulation(SIMULATION_TIME)
    sim.run()

