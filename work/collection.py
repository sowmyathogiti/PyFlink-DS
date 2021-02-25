from pyflink.common.serialization import SimpleStringEncoder
from pyflink.common.typeinfo import Types
from pyflink.datastream.connectors import StreamingFileSink
from pyflink.datastream import StreamExecutionEnvironment

def collectionsOfNumbers():
    env = StreamExecutionEnvironment.get_execution_environment()
    # env.set_python_requirements("./input.txt","./output.txt")
    ds = env.from_collection(
        collection=[0, 1, 2, 3],
        type_info=Types.INT())
    ds = ds.filter(lambda x : x % 2 == 0)
    ds = ds.map(lambda x : x*10,Types.INT()).shuffle()

    ds.add_sink(StreamingFileSink
                .for_row_format('./collectionsOfNumbers.txt', SimpleStringEncoder())
                .build())
    env.execute("tutorial_job")

if __name__ == '__main__':
    collectionsOfNumbers()
