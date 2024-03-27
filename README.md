<div align="center">

  <img src="assets/systems-logo.png">
  
# Cloud Computer Architecture
### Spring Semester 2024
### Professor: [Ana Klimovic](https://anakli.inf.ethz.ch)


<a href="#">
    <img src="https://img.shields.io/badge/Python-3.10-1cb855">
</a>
<a href="#">
    <img src="https://img.shields.io/badge/Kubernetes-v1.29.2-0388fc">
</a>
<a href="#">
    <img src="https://img.shields.io/badge/Cloud-Google-F4B400">
</a>
<br>
<a href="#">
    <img src="https://img.shields.io/badge/License-MIT-8a0023">
</a>
<br>
<a href="https://systems.ethz.ch/education/courses/2024-spring/cloud-computing-architecture.html"><strong>Explore Course Page »</strong></a>
</div>

## Project Description
This project is a part of the course Cloud Computing Architecture at ETH Zurich. The project consists of 4 parts as described below.
## Getting Started
See below each part's description and how to run it.
### Part 1:
This part focuses on performing a memcached microbenchmark on the cluster with various types of interference. The goal is to understand how different interferences affect cluster performance.
To run the benchmark, sequentially run the following commands, to deploy the cluster, setup the benchmark, run the benchmark and then delete the cluster:
```bash
$ cd part1
$ export export KOPS_STATE_STORE=gs://cca-eth-2024-group-018-ethid/
$ ./deploy_cluster.sh
$ ./setup_benchmark.sh
$ ./run_benchmark.sh
$ ./delete_cluster.sh
```

Note:
The cluster configuration is stored in the bucket `gs://cca-eth-2024-group-018-ethzid`. Make sure to replace `ethzid` with your ETH username in the following file: [part1.yaml](part1/part1.yaml)

### Part 2:
This part focuses on running various workloads from the PARSEC benchmark suite and analyzing their sensitivity to various parameters. For part 2A, various types of interference are set into place, to investigate how they affect performance. For part 2B, execution is split onto multiple threads to study the impact of parallelism. To run the benchmarks, replace {X} with either A or B for parts 2A and 2B respectivelly, and sequentially run the following commands, to deploy the cluster, run the benchmark and then delete the cluster:
```bash
$ cd part2
$ export export KOPS_STATE_STORE=gs://cca-eth-2024-group-018-<ethid>/
$ ./deploy_cluster_{X}.sh
$ ./run_benchmark_{X}.sh
$ ./delete_cluster_{X}.sh
```
Note:
The cluster configuration is stored in the bucket `gs://cca-eth-2024-group-018-ethzid`. Make sure to replace `ethzid` with your ETH username in the following files: [part2a.yaml](part2/part2a.yaml), [part2b.yaml](part2/part2b.yaml)


### Running it locally


#### Team Members:
* Aris Koutris, [akoutris@ethz.ch](mailto:akoutris@ethz.ch)
* George Manos,  [gmanos@ethz.ch](mailto:gmanos@ethz.ch)
* Maritina Tsanta, [mtsanta@ethz.ch](mailto:mtsanta@ethz.ch)
