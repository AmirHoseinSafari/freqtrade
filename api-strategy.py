from flask import Flask
from flask_restful import Resource, Api, reqparse
import run_strategy

app = Flask(__name__)
api = Api(app)


class Buy(Resource):
    def post(self):
        parser = reqparse.RequestParser()  # initialize

        parser.add_argument('ema', required=True)  # add args
        parser.add_argument('timeFrame', required=True)
        parser.add_argument('numOfCandles', required=True)

        args = parser.parse_args()  # parse arguments to dictionary

        # # create new dataframe containing new values
        # new_data = pd.DataFrame({
        #     'userId': args['ema'],
        #     'name': args['timeFrame'],
        #     'city': args['numOfCandles'],
        #     'locations': [[]]
        # })
        res = run_strategy.main_function(args['timeFrame'])
        return {'buy': res}, 200  # return data with 200 OK


class Locations(Resource):
    # methods go here
    pass


api.add_resource(Buy, '/buy')  # '/users' is our entry point for Users
api.add_resource(Locations, '/locations')  # and '/locations' is our entry point for Locations


if __name__ == '__main__':
    app.run()  # run our Flask app