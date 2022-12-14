FROM us.gcr.io/broad-dsp-gcr-public/terra-jupyter-base:1.0.0
USER root
#this makes it so pip runs as root, not the user
ENV PIP_USER=false

RUN apt-get update && apt-get install -yq --no-install-recommends \
        python3-dev && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN conda install -y -c conda-forge \
        pyfit-sne \
        python-annoy \
        hnswlib

RUN pip3 -V && \
    pip3 install numpy==1.21.1 && \
    pip3 install pandas==1.2.5 && \
    pip3 install scipy==1.7.0 && \
    pip3 install Cython==0.29.24 && \
    pip3 install pybind11==2.7.0 && \
    pip3 install scikit-image==0.18.2 && \
    pip3 install scikit-learn==0.24.2 && \
    pip3 install h5py==3.3.0 && \
    pip3 install importlib-metadata==4.6.1 && \
    pip3 install joblib==1.0.1 && \
    pip3 install psutil==5.8.0 && \
    pip3 install threadpoolctl==2.2.0 && \
    pip3 install python-igraph==0.9.6 && \
    pip3 install leidenalg==0.8.7 && \
    pip3 install lightgbm==3.2.1 && \
    pip3 install loompy==3.0.6 && \
    pip3 install matplotlib==3.4.2 && \
    pip3 install natsort==7.1.1 && \
    pip3 install numba==0.53.1 && \
    pip3 install scanorama==1.7.1 && \
    pip3 install scikit-misc==0.1.4 && \
    pip3 install seaborn==0.11.1 && \
    pip3 install statsmodels==0.12.2 && \
    pip3 install numcodecs==0.8.0 && \
    pip3 install networkx==2.5.1 && \
    pip3 install zarr==2.8.3 && \
    pip3 install anndata==0.7.6 && \
    pip3 install louvain==0.7.0 && \
    pip3 install umap-learn==0.5.1 && \
    pip3 install torch==1.9.0 && \
    pip3 install harmony-pytorch==0.1.6 && \
    pip3 install cirrocumulus==1.1.17.post1 && \
    pip3 install pegasusio==0.3.1.post2 && \
    pip3 install demuxEM==0.1.6 && \
    pip3 install forceatlas2-python==1.1 && \
    pip3 install nmf-torch==0.1.1 && \
    pip3 install pegasuspy==1.4.3

RUN wget https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.zip && \
    unzip ngrok-stable-linux-amd64.zip && \
    rm ngrok-stable-linux-amd64.zip && \
    mkdir -p /software && \
    mv ngrok /software/

ENV PATH=/software:$PATH

ENV USER jupyter
USER $USER
#we want pip to install into the user's dir when the notebook is running
ENV PIP_USER=true

ENTRYPOINT ["/opt/conda/bin/jupyter", "notebook"]
