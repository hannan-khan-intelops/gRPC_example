from concurrent import futures
import grpc
import fizzbuzz_pb2
import fizzbuzz_pb2_grpc
import pandas as pd
import socket


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
        # we will return the html string of the dataframe.
        return fizzbuzz_pb2.FizzBuzzDFReply(df=df.to_html())


def serve():
    print("Server Running...")
    # create a grpc server.
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    # add the custom Computator object we have defined to the server.
    fizzbuzz_pb2_grpc.add_ComputatorServicer_to_server(Computator(), server)
    # add the same insecure port as one the client uses for a channel.
    server.add_insecure_port('[::]:8888')
    # we print out where our server is running, to be able to set up our client correctly.
    print("Server located at: ", end='')
    print(socket.gethostbyname(socket.gethostname()))
    # start the server, and wait_for_termination.
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
