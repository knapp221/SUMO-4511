import traci
import traci.constants as tc

def control_traffic_lights():
    # List of traffic light IDs
    traffic_light_ids = ["1", "2", "5", "6"]

    # Connect to the SUMO simulation
    sumoBinary = "sumo-gui"  # Use "sumo" for command-line simulation
    sumoCmd = [sumoBinary, "-c", "/home/corey/Documents/idocs/umntc/mrepo/Python_venv/venv/project/sumo_simulations/base2x2/MySimulation.sumocfg"]  # Path to your simulation config file
    traci.start(sumoCmd)

    try:
        # Initialize simulation time
        current_time = traci.simulation.getTime()
        # Get the simulation end time from the configuration
        sim_end_time = traci.simulation.getEndTime()

        while current_time < sim_end_time:
            traci.simulationStep()

            # Example of manipulating traffic lights
            for tl_id in traffic_light_ids:
                # Get current traffic light phase
                current_phase = traci.trafficlight.getPhase(tl_id)
                print(f"Time {current_time}: Traffic light {tl_id} is in phase {current_phase}")



            # Update simulation time
            current_time = traci.simulation.getTime()
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Close the TraCI connection
        traci.close()

if __name__ == "__main__":
    control_traffic_lights()
