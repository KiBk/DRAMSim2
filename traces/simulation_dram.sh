LENGTH=28 # not 33

# Define a timestamp function
timestamp() {
  date +"%d-%H_%M_%S"
}

# Run a single test
run_dramsim() {
  # Generage a trace
  python3 ../../dram.sys/DRAMSys/library/resources/traces/script.py $1 $2 $3 2>&1 | tee -a output_dramsim.txt

  # Translate the trace
  python3 create_trace.py

  # Play and recond
  { time ../DRAMSim -t mase_script.trc -s ../system.ini -d ../ini/DDR3_micron_16M_8B_x8_sg125.ini -c $((2**$2)) -q; } 2>&1 | tee -a output_dramsim.txt

  # Parce the output
  python3 output_parser.py 2>&1 | tee -a output_dramsim.txt

  # Storing files on the server
  directory_address=/import/lab/users/bykov/dramsim-test/$(timestamp)
  ssh verdot "mkdir -p $directory_address"
  scp output*.txt verdot:$directory_address/
}

echo "New test:" | tee output_dramsim.txt

# Test run
run_dramsim 20 15 2

for ((i=22;i>=0;i=i-1)); do
  run_dramsim $i $LENGTH 2
done
# for ((i=6;i>=0;i=i-1)); do
# 	run_dramsim $i $(($LENGTH-7+i)) 2
# done
