from sotabencheval.image_classification import ImageNetEvaluator

evaluator = ImageNetEvaluator(
    # automatically compare to this paper
    model_name='ResNeXt-101-32x8d',
    paper_arxiv_id='1611.05431'
)

predictions = ... # use your model to make predictions

evaluator.add(predictions)
evaluator.save()