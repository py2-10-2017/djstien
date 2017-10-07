class Call(object):
    call_counter = 1
    def __init__(self, call_name, phone_num, call_time, call_reason):
        self.id = Call.call_counter
        self.call_name = call_name
        self.phone_num = phone_num
        self.call_time = call_time
        self.call_reason = call_reason
        Call.call_counter += 1
    
    def display_info(self):
        print "ID is ", self.id
        print "Caller name is ", self.call_name
        print "Phone number is ", self.phone_num
        print "Time was ", self.call_time
        print "Reason is ", self.call_reason
        return self

class CallCenter(object):
    def __init__(self):
        self.calls = []
        self.queue = 0
 
    def addcall(self, call):
		self.calls.append(call)
		return self

    def queue_size(self):
        print "Calls in queue: ", len(self.calls)
        for call in self.calls:
            print call.display_info()
        return self   
	    
call1 = Call("John", 5526243, "10:30 AM", "complaint")
call2 = Call("Steve", 8732571, "11:00 AM", "status check")

#call1.display_info()

#call2.display_info()

center = CallCenter()
center.addcall(call1).addcall(call2).queue_size()





