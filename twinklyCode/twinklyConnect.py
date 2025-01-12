if (DEFINE_DEVICE != ""): # 
    def timeout_handler():
        print("failed to connect: timeout") 
        os.kill(os.getpid(), signal.SIGINT) # this is here because ctrl+C didn't work
        os.kill(os.getpid(), signal.SIGSEGV)
        # exit(1)  # also didn't work

    timeout = 5  # Set your timeout duration in seconds
    timer = threading.Timer(timeout, timeout_handler)
    timer.start()

    try:
        discovered_device = xled.discover.discover()

    finally:
        timer.cancel()

    if (discovered_device.id != DEFINE_DEVICE):
        print("failed to connect: wrong device. connected: " + discovered_device.id)
        sys.exit()
    else:
        print("connected to device " + discovered_device.id)
else:
    discovered_device = xled.discover.discover()
    print("connected to device "+ discovered_device.id)



control = xled.ControlInterface(discovered_device.ip_address, discovered_device.hw_address)
control.set_mode('rt')