import pandas as pd

def process_csv(file_path):
    # Load the data
    df = pd.read_csv(file_path)
    
    # Perform some processing
    df['processed'] = df['value'] * 2  # Example transformation

    # Save the processed data
    df.to_csv('processed_' + file_path, index=False)

if __name__ == "__main__":
    process_csv('data.csv')
