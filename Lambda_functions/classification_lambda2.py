import json
import base64
import os
#from sagemaker.serializers import IdentitySerializer
#from sagemaker.predictor import Predictor

#name of deployed model
ENDPOINT = os.environ['ENDPOINT_NAME']

import boto3


def lambda_handler(event, context):

    # Decode the image data
    image_data = base64.b64decode(event["body"]["image_data"])
    
    
    runtime = boto3.Session().client('sagemaker-runtime')
    response = runtime.invoke_endpoint(EndpointName=ENDPOINT, ContentType = 'image/png',Body = image_data)
    predictions = json.loads(response['Body'].read().decode())
    
    # Make a prediction:
    #inferences = predictor.predict(image)
    
    # We return the data back to the Step Function    
    event["inferences"] = predictions
    return {
        'statusCode': 200,
        'body': json.dumps(event)
    }