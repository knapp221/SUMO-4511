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

            for tl_id in traffic_light_ids:
                # Get current phase and its remaining duration
                current_phase_index = traci.trafficlight.getPhase(tl_id)
                current_phase_duration = traci.trafficlight.getPhaseDuration(tl_id)
                current_phase_remaining = traci.trafficlight.getNextSwitch(tl_id) - current_time

                # Get the controlled lanes and links
                controlled_links = traci.trafficlight.getControlledLinks(tl_id)
                # Flatten the list of controlled lanes
                incoming_lanes = [link[0][0] for link in controlled_links if link]

                # Initialize a flag to check if vehicles are waiting
                vehicles_waiting = False

                # Check if there are vehicles waiting on red
                for lane_id in incoming_lanes:
                    # Get the vehicles on the lane
                    vehicles_on_lane = traci.lane.getLastStepVehicleIDs(lane_id)
                    for veh_id in vehicles_on_lane:
                        # Get the waiting time of the vehicle
                        waiting_time = traci.vehicle.getWaitingTime(veh_id)
                        # If the vehicle has been waiting more than a threshold, consider it waiting
                        if waiting_time > 0:
                            vehicles_waiting = True
                            break  # Exit loop if at least one vehicle is waiting
                    if vehicles_waiting:
                        break  # Exit outer loop if at least one vehicle is waiting

                # Adjust phase duration if vehicles are waiting
                if vehicles_waiting:
                    # Shorten the remaining duration of the current phase to a minimum
                    min_duration = 5  # Minimum phase duration in seconds
                    if current_phase_remaining > min_duration:
                        # Set the remaining phase duration to the minimum
                        traci.trafficlight.setPhaseDuration(tl_id, min_duration)
                else:
                    # Optionally, extend the green phase if no vehicles are waiting on red
                    pass  # You can implement logic to extend green phases here


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