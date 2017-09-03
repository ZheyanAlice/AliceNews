from cloudAMQP_client import CloudAMQPClient

CLOUDAMQP_URL = "amqp://gdflibjd:AdE_YT6zYgCy9QsPPHWf54wfMz8DbRaj@donkey.rmq.cloudamqp.com/gdflibjd"
TEST_QUEUE_NAME = "test"

def test_basic():
    client = CloudAMQPClient(CLOUDAMQP_URL, TEST_QUEUE_NAME)

    sentMsg = {"test":"test"}
    client.sendMessage(sentMsg)
    receivedMsg = client.getMessage()

    assert sentMsg == receivedMsg
    print "test_basic passed."

if __name__ == "__main__":
    test_basic()
