    from bigml.api import BigML
    api = BigML()

    source1 = api.create_source("iris.csv")
    api.ok(source1)

    dataset1 = api.create_dataset(source1, \
        {'name': 'iris dataset'})
    api.ok(dataset1)

    anomaly1 = api.create_anomaly(dataset1, \
        {'anomaly_seed': '2c249dda00fbf54ab4cdd850532a584f286af5b6',
         'name': "iris dataset's anomaly detector"})
    api.ok(anomaly1)

    batchanomalyscore1 = api.create_batch_anomaly_score(anomaly1, dataset1, \
        {'name': "Batch Anomaly Score of iris dataset's anomaly detector with iris "
                 'dataset',
         'output_dataset': True})
    api.ok(batchanomalyscore1)

    dataset2 = api.get_dataset(batchanomalyscore1['object']['output_dataset_resource'])
    api.ok(dataset2)

    dataset2 = api.update_dataset(dataset2, \
        {'fields': {'000000': {'name': 'score'}},
         'name': 'my_dataset_from_batch_anomaly_score_name'})
    api.ok(dataset2)
