import grpc
import fizzbuzz_pb2
import fizzbuzz_pb2_grpc


# easy function to just run the client and wait for a response.
def run_client():
    # create an insecure channel at port 50001.
    with grpc.insecure_channel('localhost:50001') as channel:
        # we create a stub that uses that channel.
        stub = fizzbuzz_pb2_grpc.ComputatorStub(channel)
        # we send a request and get a response from the stub.
        response = stub.ComputeFizzBuzz(fizzbuzz_pb2.FizzBuzzDFRequest(col_name="toy_example"))
    # we print the response as a markdown table.
    print("Client received the following response:")
    print(bytes(str(response), "utf-8").decode("unicode_escape"))


if __name__ == '__main__':
    run_client()