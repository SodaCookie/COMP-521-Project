from genetic.experiment import *

exp = Experiment(
    stopmethod=create_generation_stopmethod(10),
    mutation=0.2,
    mutationnum=5,
    size=10
)
exp.run()
