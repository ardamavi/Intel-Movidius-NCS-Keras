# Intel-Movidius-NCS-Keras
## Arda Mavi
Runing Keras(Background: TensorFlow) with Intel Movidius Neural Compute Stick

## The under construction!

#### Intel Movidius Neural Compute Stick

<img src="Assets/Intel_Movidius_NCS.jpg" width="500"><br/>
Thank `Mustafa Aldemir` and `Intel Corporation Turkey` very much for this gift !

# About Intel Movidius Neural Compute Stick:
Official Web Page: [developer.movidius.com](https://developer.movidius.com)

### Installing SDK command:
`git clone http://github.com/Movidius/ncsdk && cd ncsdk && make install`

### NCS Examples:
#### Installing NCS SDK's Examples command:
Run `make examples` command inside ncsdk folder.

#### For more NCS examples:
Look up: [github.com/movidius/ncappzoo](https://github.com/movidius/ncappzoo)

# Keras Model to NCS Graph:
File: keras2graph.py

Converts Keras model and weights to Intel Movidius technology internal compiled format.

`keras2graph` process turn used TensorFlow backend Keras models to NCS graph.

### But how ?
Keras Model -> TensorFlow Session -> TensorFlow Meta File -> NCS Graph

### Run Command:
`python3 keras2graph.py <Keras_Model> <Model_input_layer_name> <Model_output_layer_name> <Keras_Model_Weights> <Output_Graph>`

This command creates and saves graph file as `<Output_Graph>`.

#### Example Run Command:
`python3 keras2graph.py Keras_Model/model.json input_1 activation_7/Softmax Keras_Model/weights.h5 ./graph`

## Functions:

- [keras_to_graph](#keras_to_graph)
- [get_keras_model](#get_keras_model)
- [keras_to_tf](#keras_to_tf)
- [tf_to_graph](#tf_to_graph)

### keras_to_graph
keras_to_graph(model_path, model_in, model_out, weights_path, graph_path, take_tf_files = False)

For converting Keras Model to Movidius NCS graph.

#### Arguments:
##### Inputs:
- `model_path`: Model location. Json file. Data Type: String
- `model_in`: Name of model's input layer. Data Type: String
- `model_out`: Name of model's output layer. Data Type: String
- `graph_path`: Location of output Intel Movidius technology internal compiled format graph. Data Type: String
- `take_tf_files`: If you don't want to delete created TensorFlow model files(meta file inside), select `False`. Data Type: Bool


### get_keras_model
get_keras_model(model_path, weights_path)

For getting Keras model.

#### Arguments:
##### Inputs:
- `model_path`: Keras model Json file. Data Type: String
- `weights_path`: Weights of Keras model. h5 file. Data Type: String

##### Outputs:
- `model`: Keras model object.


### keras_to_tf
keras_to_tf(tf_model_path)

For converting Keras model to TensorFlow session and saving TensorFlow graph to meta file.

Important Note: Use this function after `get_keras_model` function.

#### Arguments:
##### Inputs:
- `tf_model_path`: Saving location of output meta file. Data Type: String


### tf_to_graph
tf_to_graph(tf_model_path, model_in, model_out, graph_path):

For converting TensorFlow graph to Intel Movidius technology internal compiled format.

#### Arguments:
##### Inputs:
- `tf_model_path`: Location of TensorFlow meta file. Data Type: String
- `model_in`: Name of model's input layer. Data Type: String
- `model_out`: Name of model's output layer. Data Type: String
- `graph_path`: Location of output Intel Movidius technology internal compiled format graph. Data Type: String


# NCS Process:
File: ncs_process.py

## Functions:

#### [All in one functions](#all-in-one-functions)
- [ready_ai_ncs](#ready_ai_ncs)
- [release_ai_ncs](#release_ai_ncs)

#### [Functions](#functions-1)
- [ncs_predict](#ncs_predict)

## All in one functions:

### ready_ai_ncs
ready_ai_ncs(graph_path, device_index=0)

For getting ready Movidius NCS with model to use with one command.

#### Arguments:
##### Inputs:
- `graph_path`: Graph file path. Data type: String
- `device_index`: Which device you want use. Data type: Int , Default value: 0
##### Outputs:
- `ncs_model`: Model object. This object ready for running graph in NCS (`ncs_model` object used with `ncs_predict()` function)
- `device`: Using device object.


### release_ai_ncs
release_ai_ncs(ncs_model, device)

For release model(in the Movidius NCS) and close Movidius device.

#### Arguments:
##### Inputs:
- `ncs_model`: Model object. (Returned from `ready_ai_ncs`)
- `device`: Using device object.


## Functions:

### ncs_predict
ncs_predict(ncs_model, inputs)

For running Intel Movidius technology internal compiled format graph in Intel Movidius NCS.

#### Arguments:
##### Inputs:
- `ncs_model`: Intel Movidius technology internal compiled format graph object.
- `inputs`: Input matrics. Data type: Numpy Array
##### Outputs:
- `outputs`: Output of graph. Data type: Numpy Array


# Important Notes:
- Install necessary modules with `sudo pip3 install -r requirements.txt` command.
