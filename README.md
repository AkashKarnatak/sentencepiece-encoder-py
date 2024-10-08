# Simple SentencePiece Encoder

A Python implementation of a simple SentencePiece encoder that reads a model file based
on the SentencePiece model protobuf definition and encodes a given string using the
model's vocabulary with the Viterbi algorithm.

# Why
Don't you wanna know what happens when the following code is run?

```py
import sentencepiece as spm
sp = spm.SentencePieceProcessor()

sp.Load('./xlnet-base-cased-spiece.model')

s = 'today is a great day'
print([sp.IdToPiece(x) for x in sp.encode(s)])
print(sp.encode(s))
```

# Info
The project relies on Protobuf files compiled from the SentencePiece model definition. To generate the necessary Python files, run the following commands:

```bash
python3 -m grpc_tools.protoc --proto_path=. --python_out=. ./sentencepiece_model.proto
python3 -m grpc_tools.protoc --proto_path=. --pyi_out=. ./sentencepiece_model.proto
```

These commands will generate the required Python files from the `.proto` file.

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests to improve the project.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
