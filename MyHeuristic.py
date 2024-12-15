# Corey Knapp
# CSCI 4511W
# Prof A. Exley
# December2024

'''
The skeleton of this code is made from CPSHeuristic.py which was made by GAI (Generative AI). The changes made from
CPSHeuristic.py are my own creation.
'''

import traci
import traci.constants as tc

def primitive_greedy_traffic_search(W, green_idle, green_non_idle, red_idle, red_non_idle):
    ps_extend = green_idle + (W * green_non_idle)
    ps_shorten = red_idle + (W * red_non_idle)
    return ps_extend > ps_shorten


def control_traffic_lights():
    # List of traffic light IDs
    traffic_light_ids = ["0", "1", "2", "3", "4", "5", "6", "7", "8"]

    # Connect to the SUMO simulation
    sumoBinary = "sumo-gui"
    sumoCmd = [sumoBinary, "-c", "/home/corey/Documents/idocs/umntc/mrepo/Python_venv/venv/project/sumo_simulations/SUMO-4511/Simulation.sumocfg"]  # Path to your simulation config file
    traci.start(sumoCmd)



    try:

        current_time = traci.simulation.getTime()
        sim_end_time = traci.simulation.getEndTime()

        # Holds total vehicle idle time
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
                if speed < 0.1:
                    vehicle_idle_times[veh_id] += traci.simulation.getDeltaT()

            # Remove vehicles that have left the simulation
            arrived_vehicles = traci.simulation.getArrivedIDList()
            for veh_id in arrived_vehicles:
                departed_vehicles.add(veh_id)

            for tl_id in traffic_light_ids:

                # Get current phase index
                current_phase_index = traci.trafficlight.getPhase(tl_id)
                current_phase_duration = traci.trafficlight.getPhaseDuration(tl_id)
                current_phase_remaining = traci.trafficlight.getNextSwitch(tl_id) - current_time

                # Retrieve the traffic light's program logic
                logic = traci.trafficlight.getAllProgramLogics(tl_id)[0]
                phases = logic.getPhases()
                current_phase = phases[current_phase_index]
                phase_state = current_phase.state

                # Get the controlled lanes and map them to signal indices
                controlled_lanes = traci.trafficlight.getControlledLanes(tl_id)
                # The list corresponds to the signal indices in the phase_state string


                g_lanes = []
                ry_lanes = []

                for idx, lane_id in enumerate(controlled_lanes):
                    signal_state = phase_state[idx]
                    if signal_state in ['G', 'g']:
                        g_lanes.append(lane_id)
                    elif signal_state in ['r', 'y', 'Y']:
                        ry_lanes.append(lane_id)


                '''
                Count idle and non-idle vehicles along oncoming intersection lanes.
                '''
                # Count all oncoming vehicles from current green phase
                idle_green = 0
                non_idle_green = 0
                for lane_id in g_lanes:
                    veh_ids = traci.lane.getLastStepVehicleIDs(lane_id)
                    for veh_id in veh_ids:
                        speed = traci.vehicle.getSpeed(veh_id)
                        if speed < 0.1:
                            idle_green += 1
                        else:
                            non_idle_green += 1

                # Count all oncoming vehicles from red and yellow phases
                idle_red = 0
                non_idle_red = 0
                for lane_id in ry_lanes:
                    veh_ids = traci.lane.getLastStepVehicleIDs(lane_id)
                    for veh_id in veh_ids:
                        speed = traci.vehicle.getSpeed(veh_id)
                        if speed < 0.1:
                            idle_red += 1
                        else:
                            non_idle_red += 1


                '''
                Adjust phase duration according to a greedy choice. A weight W can be assigned to the idle vehicles
                since they are technically more important.
                '''
                if primitive_greedy_traffic_search(0.0, idle_green, non_idle_green, idle_red, non_idle_red):
                    max_duration = 60
                    if current_phase_remaining < max_duration:
                        traci.trafficlight.setPhaseDuration(tl_id, max_duration)

                else:
                    min_duration = 5
                    if current_phase_remaining > min_duration:
                        traci.trafficlight.setPhaseDuration(tl_id, min_duration)


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

        print(f"Average vehicle idle time was: {average_idle_time:.2f} seconds")

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Close the TraCI connection
        traci.close()
if __name__ == "__main__":
    control_traffic_lights()