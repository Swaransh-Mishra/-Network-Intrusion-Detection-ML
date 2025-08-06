import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from imblearn.over_sampling import SMOTE
import joblib
import os

class NetworkDataPreprocessor:
    def __init__(self):
        self.numerical = ['duration', 'src_bytes', 'dst_bytes', 'wrong_fragment']
        self.categorical = ['protocol_type', 'service', 'flag']
        
        self.pipeline = ColumnTransformer([
            ('num', StandardScaler(), self.numerical),
            ('cat', OneHotEncoder(handle_unknown='ignore'), self.categorical)
        ])
        
        self.smote = SMOTE(sampling_strategy={
            'normal': 50000,
            'DoS': 50000,
            'probe': 15000,
            'r2l': 5000,
            'u2r': 2000
        }, random_state=42)

    def process(self, train_path, test_path):
        """Handles all preprocessing with error checking"""
        try:
            # Load data with verification
            if not os.path.exists(train_path):
                raise FileNotFoundError(f"Train file missing at {train_path}")
            if not os.path.exists(test_path):
                raise FileNotFoundError(f"Test file missing at {test_path}")
            
            train = pd.read_csv(train_path)
            test = pd.read_csv(test_path)
            
            # Verify required columns exist
            required = self.numerical + self.categorical + ['class']
            missing = [col for col in required if col not in train.columns]
            if missing:
                raise ValueError(f"Missing columns: {missing}")

            # Process data
            X_train, y_train = train.drop('class', axis=1), train['class']
            X_test, y_test = test.drop('class', axis=1), test['class']
            
            X_train_proc = self.pipeline.fit_transform(X_train)
            X_train_bal, y_train_bal = self.smote.fit_resample(X_train_proc, y_train)
            X_test_proc = self.pipeline.transform(X_test)
            
            return {
                'X_train': X_train_bal,
                'y_train': y_train_bal,
                'X_test': X_test_proc,
                'y_test': y_test
            }
            
        except Exception as e:
            print(f"Error during processing: {str(e)}")
            return None

    def save_artifacts(self, data_dict, output_dir):
        """Saves processed data with directory creation"""
        os.makedirs(output_dir, exist_ok=True)
        
        try:
            np.save(f'{output_dir}/X_train.npy', data_dict['X_train'])
            np.save(f'{output_dir}/y_train.npy', data_dict['y_train'])
            np.save(f'{output_dir}/X_test.npy', data_dict['X_test'])
            np.save(f'{output_dir}/y_test.npy', data_dict['y_test'])
            joblib.dump(self.pipeline, f'{output_dir}/preprocessor.joblib')
            print("Successfully saved all artifacts!")
        except Exception as e:
            print(f"Error saving files: {str(e)}")
