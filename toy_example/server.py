from concurrent import futures
import grpc
import fizzbuzz_pb2
import fizzbuzz_pb2_grpc
import pandas as pd


def fizzbuzz(n: int = 100) -> list():
    """
    Goes through n numbers and sees if they are divisible by
    3, 5, or both.
    Returns a list of the results.
    """
    output = []
    for i in range(n):
        if i % 15 == 0:
            output.append("FizzBuzz")
        elif i % 3 == 0:
            output.append("Fizz")
        elif i % 5 == 0:
            output.append("Buzz")
        else:
            output.append(str(i))
    return output


# create a computator object on the server side.
class Computator(fizzbuzz_pb2_grpc.ComputatorServicer):
    
    # calls the same exact function as the one in fizzbuzz_pb2_grpc.Computator
    def ComputeFizzBuzz(self, request, context):
        # only this time, it can do extra stuff, like create and edit a dataframe.
        df = pd.DataFrame()
        df[request.col_name] = fizzbuzz()
        # we will return the string of the dataframe.
        return fizzbuzz_pb2.FizzBuzzDFReply(df=df.head().to_markdown())


def serve():
    # create a grpc server.
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    # add the custom Computator object we have defined to the server.
    fizzbuzz_pb2_grpc.add_ComputatorServicer_to_server(Computator(), server)
    # add the same insecure port as the client.
    server.add_insecure_port('[::]:50001')
    # start the server, and wait_for_termination.
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    print("Server Running...")
    serve()
