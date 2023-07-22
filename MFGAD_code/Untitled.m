% Load Fisher's iris data
load fisheriris

% Split the data into training and testing sets
rng(1); % For reproducibility
indices = crossvalind('Kfold',species,10);
training = (indices <= 7);
testing = (indices > 7);

% Train the classifier
NBModel = fitcnb(meas(training,:),species(training));

% Make predictions for the testing data
predictions = predict(NBModel,meas(testing,:));

% Evaluate the accuracy of the predictions
confusionmat(species(testing),predictions)