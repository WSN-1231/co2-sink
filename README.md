# co2-sink
Code for WSN's sink in Raspberry Pi

## Structure

```bash
|-- packet.py		// encapsulating parsed data into JSON
|-- serial_conn.py	// configuring serial connection to Sink Node
 -- sendData.py		// sending JSON to webservice

```

## How To Use

1. Open 'sendData.py' with text editor, set several variables:
- hostname : server's API address for storing data
- baudrate : baudrate used in sink sensor node for serial connection via USB
- timeout  : timeout period for serial connection

2. Run 'sendData.py' with command:

```bash
python sendData.py
```

