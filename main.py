from genetic.experiment import *

exp = Experiment(
    stopmethod=create_generation_stopmethod(1),
    mutation=0.2,
    mutationnum=5,
    gameruns=1,
    size=1
)
exp.run()
