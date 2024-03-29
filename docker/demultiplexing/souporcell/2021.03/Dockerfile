FROM continuumio/miniconda3:4.10.3
SHELL ["/bin/bash", "-c"]

RUN apt-get update && \
    apt-get install -y wget build-essential curl libncurses5-dev zlib1g-dev libbz2-dev liblzma-dev git unzip && \
    apt-get install --no-install-recommends -y gnupg && \
    echo "deb [signed-by=/usr/share/keyrings/cloud.google.gpg] http://packages.cloud.google.com/apt cloud-sdk main" | tee -a /etc/apt/sources.list.d/google-cloud-sdk.list && \
    curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key --keyring /usr/share/keyrings/cloud.google.gpg add - && \
    apt-get update -y && apt-get install -y google-cloud-cli=392.0.0-0 && \
    apt-get -qq -y autoremove && \
    apt-get clean

RUN curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64-2.7.11.zip" -o "awscliv2.zip" && \
    unzip awscliv2.zip && \
    ./aws/install && \
    rm awscliv2.zip

RUN cd /opt && \
    wget -O minimap2.tar.gz https://github.com/lh3/minimap2/archive/v2.7.tar.gz && \
    mkdir minimap2 && \
    tar -zxvf minimap2.tar.gz -C minimap2 --strip-components 1 && \
    rm minimap2.tar.gz && \
    cd minimap2 && \
    make

ENV PATH=/opt/minimap2/:$PATH

RUN cd /opt && \
    wget -O bedtools.tar.gz https://github.com/arq5x/bedtools2/releases/download/v2.28.0/bedtools-2.28.0.tar.gz && \
    mkdir bedtools2 && \
    tar -zxvf bedtools.tar.gz -C bedtools2 --strip-components 1 && \
    rm bedtools.tar.gz && \
    cd bedtools2 && \
    make

ENV PATH=/opt/bedtools2/bin:$PATH

ENV CARGO_HOME=/opt/.cargo
ENV RUSTUP_HOME=/opt/.cargo

RUN bash -c 'curl https://sh.rustup.rs -sSf | sh -s -- -y'

ENV PATH=/opt/.cargo/bin:$PATH

RUN cd /opt && \
    wget https://github.com/wheaton5/souporcell/archive/1bd9f11d70eaee6ac14713de09c377c285ca2787.zip -O souporcell.zip && \
    unzip souporcell.zip && \
    rm souporcell.zip && \
    mv souporcell-1bd9f11d70eaee6ac14713de09c377c285ca2787 souporcell && \
    cd souporcell/troublet && \
    cargo build --release && \
    cd /opt/souporcell/souporcell && \
    cargo build --release

ENV PATH=/opt/souporcell:/opt/souporcell/troublet/target/release:$PATH

RUN conda install -y python=3.6.13 && \
    conda install -y -c conda-forge mamba=0.17.0 && \
    mamba install -y -c conda-forge numpy=1.19.5 pandas=1.1.5 scipy=1.5.3 pyvcf=0.6.8 pystan=2.19.1.1 anndata=0.7.6 zarr=2.8.3 networkx=2.5.1 && \
    mamba install -y -c bioconda pysam=0.16.0.1 pyfaidx=0.6.2 pegasusio=0.2.10 scanpy

RUN pip install stratocumulus==0.1.7

RUN cd /opt && \
    wget -O htslib.tar.bz2 https://github.com/samtools/htslib/releases/download/1.9/htslib-1.9.tar.bz2 && \
    mkdir htslib && \
    tar -xvjf htslib.tar.bz2 -C htslib --strip-components 1 && \
    rm htslib.tar.bz2 && \
    cd htslib && \
    ./configure && \
    make && \
    make install

RUN cd /opt && \
    wget -O samtools.tar.bz2 https://github.com/samtools/samtools/releases/download/1.9/samtools-1.9.tar.bz2 && \
    mkdir samtools && \
    tar -xvjf samtools.tar.bz2 -C samtools --strip-components 1 && \
    rm samtools.tar.bz2 && \
    cd samtools && \
    ./configure && \
    make && \
    make install

RUN cd /opt && \
    wget -O bcftools.tar.bz2 https://github.com/samtools/bcftools/releases/download/1.9/bcftools-1.9.tar.bz2 && \
    mkdir bcftools && \
    tar -xvjf bcftools.tar.bz2 -C bcftools --strip-components 1 && \
    rm bcftools.tar.bz2 && \
    cd bcftools && \
    ./configure && \
    make && \
    make install

RUN cd /opt && \
    wget -O freebayes https://github.com/ekg/freebayes/releases/download/v1.3.1/freebayes-v1.3.1 && \
    chmod 777 freebayes

RUN cd /opt && \
    wget https://github.com/10XGenomics/vartrix/releases/download/v1.1.16/vartrix_linux && \
    mv vartrix_linux vartrix && \
    chmod 777 vartrix

ADD https://raw.githubusercontent.com/lilab-bcb/cumulus/master/docker/demultiplexing/souporcell/extract_barcodes_from_rna.py /opt
ADD https://raw.githubusercontent.com/lilab-bcb/cumulus/master/docker/demultiplexing/souporcell/match_donors.py /opt

ADD https://raw.githubusercontent.com/lilab-bcb/cumulus/master/docker/monitor_script.sh /opt
RUN chmod a+rx /opt/monitor_script.sh

ENV PATH=/opt/vartrix:/opt:$PATH
