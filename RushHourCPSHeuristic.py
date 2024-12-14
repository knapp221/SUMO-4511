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

                # Initialize idle time if vehicle recently added.
                if veh_id not in vehicle_idle_times:
                    vehicle_idle_times[veh_id] = 0.0

                # increment idle time
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
                controlled_lanes = traci.trafficlight.getControlledLanes(tl_id)  # List of lanes
                # The list corresponds to the signal indices in the phase_state string

                # Map signal indices to lanes
                g_lanes = []
                ry_lanes = []

                for idx, lane_id in enumerate(controlled_lanes):
                    signal_state = phase_state[idx]
                    if signal_state in ['G', 'g']:
                        g_lanes.append(lane_id)
                    elif signal_state in ['r', 'y', 'Y']:
                        ry_lanes.append(lane_id)
                    # Handle other signal states if necessary

                # Count vehicles waiting on green lanes
                vehicles_waiting_green = 0
                for lane_id in g_lanes:
                    vehicles_on_lane = traci.lane.getLastStepVehicleIDs(lane_id)
                    for veh_id in vehicles_on_lane:
                        waiting_time = traci.vehicle.getWaitingTime(veh_id)
                        if waiting_time > 0:
                            vehicles_waiting_green += 1

                # Count vehicles waiting on red lanes
                vehicles_waiting_red = 0
                for lane_id in ry_lanes:
                    vehicles_on_lane = traci.lane.getLastStepVehicleIDs(lane_id)
                    for veh_id in vehicles_on_lane:
                        waiting_time = traci.vehicle.getWaitingTime(veh_id)
                        if waiting_time > 0:
                            vehicles_waiting_red += 1


                '''
                Adjust phase duration as appropriate by number of idle vehicles or whether it is morning/afternoon
                rush hour. 
                '''
                timeOfDay = "morning_RH"

                if timeOfDay == "morning_RH":

                    if vehicles_waiting_red > vehicles_waiting_green:

                        # More vehicles waiting on red
                        min_duration = 5
                        if current_phase_remaining > min_duration:
                            traci.trafficlight.setPhaseDuration(tl_id, min_duration)

                    elif vehicles_waiting_green > vehicles_waiting_red:
                        # More vehicles on green
                        max_duration = 60
                        if current_phase_remaining < max_duration:
                            traci.trafficlight.setPhaseDuration(tl_id, max_duration)

                    timeOfDay = "noon"

                elif timeOfDay == "noon":
                    if vehicles_waiting_red > vehicles_waiting_green:

                        # More vehicles waiting on red
                        min_duration = 5
                        if current_phase_remaining > min_duration:
                            traci.trafficlight.setPhaseDuration(tl_id, min_duration)

                    elif vehicles_waiting_green > vehicles_waiting_red:
                        # More vehicles on green
                        max_duration = 60
                        if current_phase_remaining < max_duration:
                            traci.trafficlight.setPhaseDuration(tl_id, max_duration)

                    timeOfDay = "afternoon_RH"


                elif timeOfDay == "afternoon_RH":
                    if vehicles_waiting_red > vehicles_waiting_green:
                        # More vehicles waiting on red
                        min_duration = 5
                        if current_phase_remaining > min_duration:
                            traci.trafficlight.setPhaseDuration(tl_id, min_duration)

                    elif vehicles_waiting_green > vehicles_waiting_red:
                        # More vehicles on green
                        max_duration = 60
                        if current_phase_remaining < max_duration:
                            traci.trafficlight.setPhaseDuration(tl_id, max_duration)

                    timeOfDay = "evening"


                elif timeOfDay == "noon":
                    if vehicles_waiting_red > vehicles_waiting_green:
                        # More vehicles waiting on red
                        min_duration = 5
                        if current_phase_remaining > min_duration:
                            traci.trafficlight.setPhaseDuration(tl_id, min_duration)

                    elif vehicles_waiting_green > vehicles_waiting_red:

                        # More vehicles on green
                        max_duration = 60
                        if current_phase_remaining < max_duration:
                            traci.trafficlight.setPhaseDuration(tl_id, max_duration)

                    timeOfDay = "morning_RH"



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