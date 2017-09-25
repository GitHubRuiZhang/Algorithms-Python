# Uses python3
# Network packet processing simulation
# Input:
# size of the buffer: S; number of incoming network packages: n
# n lines: time of arrival: A_i; the processing time: P_i
# Output:
# n lines: -1 if dropped, otherwise the time to process it

# Example:
# Input:
# 1 0
# Output:

# Example:
# Input:
# 1 1
# 0 0
# Output:
# 0

# Example:
# Input:
# 1 2
# 0 1
# 0 1
# Output:
# 0
# -1

# Example:
# Input:
# 1 2
# 0 1
# 1 1
# Output:
# 0
# 1

# Solution Methods:
# list or queue


class Request:
    def __init__(self, arrival_time, process_time):
        self.arrival_time = arrival_time
        self.process_time = process_time


class Response:
    def __init__(self, dropped, start_time):
        self.dropped = dropped
        self.start_time = start_time


class Buffer:
    def __init__(self, size):
        self.size = size
        self.finish_time_ = []

    def Process(self, request):
        if (self.finish_time_ == []):
            self.size -= 1
            self.finish_time_.append(request.arrival_time + request.process_time)
            return Response(False, request.arrival_time)
        elif (request.arrival_time > self.finish_time_[-1]):
            self.size += len(self.finish_time_) - 1
            self.finish_time = []
            self.finish_time_.append(request.arrival_time + request.process_time)
            return Response(False, request.arrival_time)
        else:
            for i in range(len(self.finish_time_)):
                if request.arrival_time > self.finish_time_[-1 - i]:
                    self.size += len(self.finish_time_) - i
                    del self.finish_time_[:(len(self.finish_time_) - i)]
                    break
                elif request.arrival_time == self.finish_time_[-1 - i]:
                    self.size += len(self.finish_time_) - i - 2
                    del self.finish_time_[:(len(self.finish_time_) - i - 1)]
                    self.finish_time_.append(self.finish_time_[-1] + request.process_time)
                    return Response(False, self.finish_time_[-2])

            if self.size == 0:
                return Response(True, -1)
            else:
                self.size -= 1
                self.finish_time_.append(self.finish_time_[-1] + request.process_time)
                return Response(False, self.finish_time_[-2])

    def Process_Fast(self, request):
        if (self.finish_time_ == []):
            self.size -= 1
            self.finish_time_.append(request.arrival_time + request.process_time)
            return Response(False, request.arrival_time)
        elif (request.arrival_time > self.finish_time_[-1]):
            self.size += len(self.finish_time_) - 1
            self.finish_time = []
            self.finish_time_.append(request.arrival_time + request.process_time)
            return Response(False, request.arrival_time)
        else:
            for i in range(len(self.finish_time_)):
                if request.arrival_time < self.finish_time_[i]:
                    self.size += i
                    del self.finish_time_[:i]
                    break
                elif request.arrival_time == self.finish_time_[i]:
                    if len(self.finish_time_) == 1:
                        timeIns = self.finish_time_[0]
                        del self.finish_time_[0]
                        self.finish_time_.append(timeIns + request.process_time)
                        return Response(False, timeIns)
                    else:
                        self.size += i
                        del self.finish_time_[:(i + 1)]
                        self.finish_time_.append(self.finish_time_[-1] + request.process_time)
                        return Response(False, self.finish_time_[-2])

            if self.size == 0:
                return Response(True, -1)
            else:
                self.size -= 1
                self.finish_time_.append(self.finish_time_[-1] + request.process_time)
                return Response(False, self.finish_time_[-2])


def ReadRequests(count):
    requests = []
    for i in range(count):
        arrival_time, process_time = map(int, input().strip().split())
        requests.append(Request(arrival_time, process_time))
    return requests


def ProcessRequests(requests, buffer):
    responses = []
    for request in requests:
        responses.append(buffer.Process_Fast(request))
    return responses


def PrintResponses(responses):
    for response in responses:
        print(response.start_time if not response.dropped else -1)


if __name__ == "__main__":
    size, count = map(int, input().strip().split())
    requests = ReadRequests(count)
    buffer = Buffer(size)
    responses = ProcessRequests(requests, buffer)
    PrintResponses(responses)
