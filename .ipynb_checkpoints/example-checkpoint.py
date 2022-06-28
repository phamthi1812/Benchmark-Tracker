print("Tracking for training start !!!!")
now = datetime.now()
# dd/mm/YY H:M:S
dt_string = now.strftime("%d:%m:%Y_%H:%M:%S")    
for i in range(0,20):
    experiment[i] = os.mkdir("logPath/"+dt_string"_%d"%i)
    #tmp_dir = tempfile.mkdtemp()
    # Init tracker with log path
    #tracker = ImpactTracker("logPath/"+dt_string)
    # Start tracker in a separate process
    #tracker.launch_impact_monitor()
    with ImpactTracker("logPath/"+dt_string"_%d"%i):
        benchmark = AIBenchmark(use_CPU=None)
        results = benchmark.run()
    
    tracker_results = {}
    data_interface = DataInterface(["logPath/"+dt_string"_%d"%i])
    tracker_results["tool_energy_consumption(kWh)"]=data_interface.total_power
    tracker_results["tool_carbon_emissions(kgC02eq)"]=data_interface.kg_carbon
    tracker_results["tool_duration(seconds)"]=data_interface.exp_len_hours*3600
    tracker_results["tool_PUE"]=data_interface.PUE
    print(results)
