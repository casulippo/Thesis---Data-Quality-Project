FROM jupyter/datascience-notebook
COPY requirements.txt ./
RUN pip install -r requirements.txt
RUN conda install -c conda-forge jupyter_contrib_nbextensions
RUN jupyter nbextension enable toc2/main && \
    jupyter nbextension enable varInspector/main && \
    jupyter nbextension enable python-markdown/main && \
    jupyter nbextension enable hide_input_all/main && \
    jupyter nbextension enable --py widgetsnbextension