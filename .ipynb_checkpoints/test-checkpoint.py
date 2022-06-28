import os
os.environ["CUDA_VISIBLE_DEVICES"]="0,1"

import ai_benchmark
benchmark = ai_benchmark.AIBenchmark(use_CPU=None)
results = benchmark.run()
