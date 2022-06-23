from ai_benchmark.utils import *

import sys
import os
import time
import tempfile
from datetime import datetime
import torch

from experiment_impact_tracker.compute_tracker import ImpactTracker
from experiment_impact_tracker.data_interface import DataInterface


class AIBenchmark:

    def __init__(self, use_CPU=None, verbose_level=1):

        self.tf_ver_2 = parse_version(tf.__version__) > parse_version('1.99')
        self.verbose = verbose_level

        if verbose_level > 0:
            printIntro()

        np.warnings.filterwarnings('ignore')

        try:

            if verbose_level < 3:

                os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

                if self.tf_ver_2:
                    import logging
                    logger = tf.get_logger()
                    logger.disabled = True
                    logger.setLevel(logging.ERROR)

                elif parse_version(tf.__version__) > parse_version('1.13'):
                    tf.compat.v1.logging.set_verbosity(tf.compat.v1.logging.ERROR)

                else:
                    tf.logging.set_verbosity(tf.logging.ERROR)

            else:

                if self.tf_ver_2:
                    import logging
                    logger = tf.get_logger()
                    logger.disabled = True
                    logger.setLevel(logging.INFO)

                elif parse_version(tf.__version__) > parse_version('1.13'):
                    tf.compat.v1.logging.set_verbosity(tf.compat.v1.logging.INFO)

                else:
                    tf.logging.set_verbosity(tf.logging.INFO)

        except:
            pass

        np.random.seed(42)
        self.cwd = path.dirname(__file__)

        self.use_CPU = False
        if use_CPU:
            self.use_CPU = True

    def run(self, precision="normal"):
        return run_tests(training=True, inference=True, micro=False, verbose=self.verbose,
                         use_CPU=self.use_CPU, precision=precision, _type="full", start_dir=self.cwd)
    def run_training(self, precision="normal"):
        return run_tests(training=True, inference=False, micro=False, verbose=self.verbose,
                         use_CPU=self.use_CPU, precision=precision, _type="training", start_dir=self.cwd)

os.environ["CUDA_VISIBLE_DEVICES"]="0,1"

if __name__ == "__main__":    
    benchmark = AIBenchmark(use_CPU=None)
    # for all inference and training
    results = benchmark.run()
    # for just training
    #results = benchmark.run_training()
