# Introduction to API getHistoricalImagesOfMarker

### Received body of json format

> e.g.
> 
> {
>  "body": "{\"markerId\":\"7d1c6bac-06a2-4af2-9fb9-a8308c464f1b\"}"
> }

### Returned body of json format

> e.g.
> 
> case1: when can't access table of database
> 
> ```
> { 
>   'statusCode': 500,  
>   'body': json.dumps({'error': 'Server configuration error.'})  
> }  
> ```
> 
> case2: when can't find "markerId" in request body
> 
> ```
> {  
>   'statusCode': 400,  
>   'body': json.dumps({'error': 'markerId is required.'})  
> }  
> ```
> 
> case3: when json string in request body is invalid
> 
> ```
> {  
>   'statusCode': 400,  
>   'body': json.dumps({'error': 'Invalid request body.'})  
> }  
> ```
> 
> case4: when location marker is not found in database
> 
> ```
> {  
>   'statusCode': 404,  
>   'body': json.dumps({'error': 'Location marker not found.'})  
> }  
> ```
> 
> case5: when for given marker, the historical images is empty or a empty array in database
> 
> ```
> {  
>   'statusCode': 404,  
>   'body': json.dumps({'error': 'Historical images unavailable.'})  
> }  
> ```
> 
> case6: success get all historical images
> 
> ```
> {  
>   'statusCode': 200,  
>   'body': json.dumps({  
>   'markerId': marker.get_marker_id(),  
>   'historicalImages': [image.to_json() for image in historical_images]  
> })  
> ```
> 
> case7: others errors occur
> 
> ```
> {  
>   'statusCode': 500,  
>   'body': json.dumps({'error': 'Failed to retrieve historical images.'})  
> }
> ```
> 
> .
