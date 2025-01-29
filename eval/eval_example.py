from ragas.dataset_schema import SingleTurnSample
from ragas.metrics._string import DistanceMeasure, NonLLMStringSimilarity

sample = SingleTurnSample(
    response="The Eiffel Tower is located in India.", reference="The Eiffel Tower is located in Paris."
)

scorer = NonLLMStringSimilarity(distance_measure=DistanceMeasure.LEVENSHTEIN)
print(scorer.single_turn_score(sample))
