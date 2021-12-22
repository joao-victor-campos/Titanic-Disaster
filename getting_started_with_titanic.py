{"metadata":{"kernelspec":{"language":"python","display_name":"Python 3","name":"python3"},"language_info":{"pygments_lexer":"ipython3","nbconvert_exporter":"python","version":"3.6.4","file_extension":".py","codemirror_mode":{"name":"ipython","version":3},"name":"python","mimetype":"text/x-python"}},"nbformat_minor":4,"nbformat":4,"cells":[{"cell_type":"code","source":"# %% [code] {\"execution\":{\"iopub.status.busy\":\"2021-12-21T22:20:27.095536Z\",\"iopub.execute_input\":\"2021-12-21T22:20:27.095865Z\",\"iopub.status.idle\":\"2021-12-21T22:20:27.134848Z\",\"shell.execute_reply.started\":\"2021-12-21T22:20:27.095784Z\",\"shell.execute_reply\":\"2021-12-21T22:20:27.134223Z\"},\"jupyter\":{\"outputs_hidden\":false}}\n# This Python 3 environment comes with many helpful analytics libraries installed\n# It is defined by the kaggle/python Docker image: https://github.com/kaggle/docker-python\n# For example, here's several helpful packages to load\n\nimport numpy as np # linear algebra\nimport pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)\n\n# Input data files are available in the read-only \"../input/\" directory\n# For example, running this (by clicking run or pressing Shift+Enter) will list all files under the input directory\n\nimport os\nfor dirname, _, filenames in os.walk('/kaggle/input'):\n    for filename in filenames:\n        print(os.path.join(dirname, filename))\n\n# You can write up to 20GB to the current directory (/kaggle/working/) that gets preserved as output when you create a version using \"Save & Run All\" \n# You can also write temporary files to /kaggle/temp/, but they won't be saved outside of the current session\n\n# %% [code] {\"execution\":{\"iopub.status.busy\":\"2021-12-21T22:21:51.625991Z\",\"iopub.execute_input\":\"2021-12-21T22:21:51.626226Z\",\"iopub.status.idle\":\"2021-12-21T22:21:51.665021Z\",\"shell.execute_reply.started\":\"2021-12-21T22:21:51.626200Z\",\"shell.execute_reply\":\"2021-12-21T22:21:51.664026Z\"},\"jupyter\":{\"outputs_hidden\":false}}\ntrain_data = pd.read_csv(\"/kaggle/input/titanic/train.csv\")\ntrain_data.head()\n\n# %% [code] {\"execution\":{\"iopub.status.busy\":\"2021-12-21T22:26:30.887546Z\",\"iopub.execute_input\":\"2021-12-21T22:26:30.887808Z\",\"iopub.status.idle\":\"2021-12-21T22:26:30.914298Z\",\"shell.execute_reply.started\":\"2021-12-21T22:26:30.887779Z\",\"shell.execute_reply\":\"2021-12-21T22:26:30.913564Z\"},\"jupyter\":{\"outputs_hidden\":false}}\ntest_data = pd.read_csv(\"/kaggle/input/titanic/test.csv\")\ntest_data.head()\n\n# %% [code] {\"execution\":{\"iopub.status.busy\":\"2021-12-21T22:43:09.183332Z\",\"iopub.execute_input\":\"2021-12-21T22:43:09.183607Z\",\"iopub.status.idle\":\"2021-12-21T22:43:09.190430Z\",\"shell.execute_reply.started\":\"2021-12-21T22:43:09.183579Z\",\"shell.execute_reply\":\"2021-12-21T22:43:09.189875Z\"},\"jupyter\":{\"outputs_hidden\":false}}\nwomen = train_data.loc[train_data.Sex == 'female'][\"Survived\"]\nrate_women = sum(women)/len(women)\n                    \nprint(\"% of women who survived:\", rate_women)\n\n# %% [code] {\"execution\":{\"iopub.status.busy\":\"2021-12-21T22:43:32.982622Z\",\"iopub.execute_input\":\"2021-12-21T22:43:32.982887Z\",\"iopub.status.idle\":\"2021-12-21T22:43:32.991047Z\",\"shell.execute_reply.started\":\"2021-12-21T22:43:32.982857Z\",\"shell.execute_reply\":\"2021-12-21T22:43:32.990388Z\"},\"jupyter\":{\"outputs_hidden\":false}}\nmen = train_data.loc[train_data.Sex == 'male'][\"Survived\"]\nrate_men = sum(men)/len(men)\n\nprint(\"% of men who survived:\", rate_men)\n\n# %% [code] {\"execution\":{\"iopub.status.busy\":\"2021-12-21T22:59:18.610988Z\",\"iopub.execute_input\":\"2021-12-21T22:59:18.611214Z\",\"iopub.status.idle\":\"2021-12-21T22:59:19.919775Z\",\"shell.execute_reply.started\":\"2021-12-21T22:59:18.611192Z\",\"shell.execute_reply\":\"2021-12-21T22:59:19.918577Z\"},\"jupyter\":{\"outputs_hidden\":false}}\nfrom sklearn.ensemble import RandomForestClassifier\n\ny = train_data[\"Survived\"]\n\nfeatures = [\"Pclass\", \"Sex\", \"SibSp\", \"Parch\"]\nX = pd.get_dummies(train_data[features])\nX_test = pd.get_dummies(test_data[features])\n\nmodel = RandomForestClassifier(n_estimators=100, max_depth=5, random_state=1)\nmodel.fit(X, y)\npredictions = model.predict(X_test)\n\noutput = pd.DataFrame({'PassengerId': test_data.PassengerId, 'Survived': predictions})\noutput.to_csv('submission.csv', index=False)\nprint(\"Your submission was successfully saved!\")","metadata":{"_uuid":"cb6e673e-6bc5-4458-a364-52920242e5a3","_cell_guid":"7ada6294-f210-49be-97fe-cc990431c814","collapsed":false,"jupyter":{"outputs_hidden":false},"trusted":true},"execution_count":null,"outputs":[]}]}