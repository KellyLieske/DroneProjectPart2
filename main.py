
import sys
import boto3



def createTable(tableName, client):
    res = client.create_table(
        #In table creation we only include the partition key and sort key,
        # we can add the other attributes later when we insert records
        AttributeDefinitions=[{
            'AttributeName': 'isValidFlight',
            'AttributeType' : 'S',

            },
            {
                'AttributeName': 'flightKey',
                'AttributeType': 'S',

            },

        ],
        KeySchema=[
            {
                'AttributeName': 'isValidFlight',
                'KeyType': 'HASH',
            },
            {
                'AttributeName': 'flightKey',
                'KeyType': 'RANGE',
            },
        ],

        ProvisionedThroughput = {
                              'ReadCapacityUnits': 5,
                              'WriteCapacityUnits': 5,
                          },
        TableName=tableName,
    )
    #print(res)



def insertData(client):

    isValid = ""
    if sys.argv[1] is "Y":
        isValid = "Valid"
    elif sys.argv[1] is "N":
        isValid = "Invalid"

    key  = sys.argv[2] + '+' +  sys.argv[3] + '+' + sys.argv[4]

    name = sys.argv[5]
    dept = sys.argv[6]

    client.put_item(
        Item = {

           "isValidFlight" : {
               "S" : isValid
           },
            "flightKey": {
                "S": key
            },
            "fullName": {
                "S": name
            },
            "Department" : {
                "S": dept
            },


        }
        ,
        TableName = "FlightData"

    )



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    dynamo = boto3.client('dynamodb')
    list_tables = dynamo.list_tables()['TableNames']

    if 'FlightData' not in list_tables:
        createTable('FlightData', dynamo)

    list_tables = dynamo.list_tables()['TableNames']

    if len(sys.argv) == 7:
        if 'FlightData' in list_tables:
                insertData(dynamo)
        else:
            print("Error!")


    res = dynamo.scan(
        TableName="FlightData",
    )
    #First printout shows all items sorted by
    for item in res['Items']:
        print("Is Valid flight?: " + item['isValidFlight']['S'] + " Flight Key " + item['flightKey']['S'])
    # Queries aws to only get valid flights
    res = dynamo.query(
        TableName="FlightData",
        ExpressionAttributeValues={
        ':v1': {
            'S': 'Valid',
        },
    },
        KeyConditionExpression='isValidFlight = :v1',

    )

    print()
    # for item in res['Items']:
    #     print(item)
    for item in res['Items']:
        print("Valid flight?:" + item['isValidFlight']['S'] + " Flight Key " + item['flightKey']['S'] + " Name of Pilot: " + item['fullName']['S'] + " Dept : " + item['Department']['S'] )




