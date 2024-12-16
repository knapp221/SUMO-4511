'''
GAI NOTE: MOST OF THE CODE IN THIS PYTHON FILE WERE PROVIDED BY A GAI; CHATGPT, ACCESSED NOVEMBER 2024.
THE CODE HAS BEEN UTILIZED AND WORKS AS INTENDED, BUT I DO NOT TAKE ANY CREDIT FOR ITS CREATION.
'''

import traci
import traci.constants as tc

def control_traffic_lights():
    # List of traffic light IDs
    traffic_light_ids = ["0", "1", "2", "3", "4", "5", "6", "7", "8"]

    # Connect to the SUMO simulation
    sumoBinary = "sumo-gui"
    sumoCmd = [sumoBinary, "-c", "/home/corey/Documents/idocs/umntc/mrepo/Python_venv/venv/project/sumo_simulations/SUMO-4511/Simulation.sumocfg"]  # Path to your simulation config file
    traci.start(sumoCmd)

    try:
        # Initialize simulation time
        current_time = traci.simulation.getTime()
        # Get the simulation end time from the configuration
        sim_end_time = traci.simulation.getEndTime()

        # Dictionary to store idle times for each vehicle
        vehicle_idle_times = {}
        # Set to keep track of vehicles that have left the simulation
        departed_vehicles = set()

        while current_time < sim_end_time:
            traci.simulationStep()

            # Get the list of vehicle IDs currently in the simulation
            vehicle_ids = traci.vehicle.getIDList()

            # Update idle times for each vehicle
            for veh_id in vehicle_ids:
                # Get the speed of the vehicle
                speed = traci.vehicle.getSpeed(veh_id)

                # Initialize idle time if vehicle is new
                if veh_id not in vehicle_idle_times:
                    vehicle_idle_times[veh_id] = 0.0

                # If speed is zero, increment idle time
                if speed < 0.1:  # Considering speeds less than 0.1 m/s as idle
                    vehicle_idle_times[veh_id] += traci.simulation.getDeltaT()

            # Remove vehicles that have left the simulation
            arrived_vehicles = traci.simulation.getArrivedIDList()
            for veh_id in arrived_vehicles:
                departed_vehicles.add(veh_id)
            '''
            # Example of manipulating traffic lights
            for tl_id in traffic_light_ids:
                # Get current traffic light phase
                current_phase = traci.trafficlight.getPhase(tl_id)

                # Retrieve the traffic light's program logic
                logic = traci.trafficlight.getAllProgramLogics(tl_id)[0]
                phases = logic.getPhases()
                num_phases = len(phases)

                # Custom logic: Change to the next phase every 30 seconds
                if current_time % 30 == 0:
                    # Switch to the next phase
                    next_phase = (current_phase + 1) % num_phases
                    traci.trafficlight.setPhase(tl_id, next_phase)
            '''
            # Update simulation time
            current_time = traci.simulation.getTime()

        # After the simulation ends, calculate average idle time
        total_idle_time = 0.0
        total_vehicles = len(vehicle_idle_times)

        for veh_id in vehicle_idle_times:
            total_idle_time += vehicle_idle_times[veh_id]

        if total_vehicles > 0:
            average_idle_time = total_idle_time / total_vehicles
        else:
            average_idle_time = 0.0

        print(f"Average Vehicle Idle Time: {average_idle_time:.2f} seconds")

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Close the TraCI connection
        traci.close()
if __name__ == "__main__":
    control_traffic_lights()