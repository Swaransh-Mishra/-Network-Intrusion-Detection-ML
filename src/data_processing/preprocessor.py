import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from imblearn.over_sampling import SMOTE
import joblib

class NetworkDataPreprocessor:
    def __init__(self):
        # Define feature types
        self.numerical = [
            'duration', 'src_bytes', 'dst_bytes',
            'wrong_fragment', 'hot', 'num_failed_logins'
        ]
        
        self.categorical = [
            'protocol_type', 'service', 'flag'
        ]
        
        # Build processing pipeline
        self.pipeline = ColumnTransformer([
            ('num', StandardScaler(), self.numerical),
            ('cat', OneHotEncoder(handle_unknown='ignore'), self.categorical)
        ])
        
        # SMOTE configuration
        self.smote = SMOTE(sampling_strategy={
            'normal': 50000,
            'DoS': 50000,
            'probe': 15000,
            'r2l': 5000,
            'u2r': 2000
        }, random_state=42)

    def process(self, train_path, test_path):
        """Main preprocessing workflow"""
        # Load data
        train = pd.read_csv(train_path)
        test = pd.read_csv(test_path)
        
        # Separate features/target
        X_train, y_train = train.drop('class', axis=1), train['class']
        X_test, y_test = test.drop('class', axis=1), test['class']
        
        # Fit and transform training data
        X_train_proc = self.pipeline.fit_transform(X_train)
        X_train_bal, y_train_bal = self.smote.fit_resample(X_train_proc, y_train)
        
        # Transform test data (no fitting)
        X_test_proc = self.pipeline.transform(X_test)
        
        return {
            'X_train': X_train_bal,
            'y_train': y_train_bal,
            'X_test': X_test_proc,
            'y_test': y_test
        }

    def save_artifacts(self, output_dir):
        """Save pipeline and example data"""
        joblib.dump(self.pipeline, f'{output_dir}/preprocessor.joblib')