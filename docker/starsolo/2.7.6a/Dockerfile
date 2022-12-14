FROM debian:buster-slim
SHELL ["/bin/bash", "-c"]

RUN apt-get -qq update && \
    apt-get -qq -y install --no-install-recommends \
        wget \
        build-essential \
        curl \
        unzip \
        gnupg \
        python3 \
        python3-pip

RUN pip3 install --upgrade pip --no-cache-dir && \
    pip3 install numpy==1.21.0 --no-cache-dir && \
    pip3 install pandas==1.2.5 --no-cache-dir && \
    pip3 install stratocumulus==0.1.1 --no-cache-dir 

RUN echo "deb [signed-by=/usr/share/keyrings/cloud.google.gpg] http://packages.cloud.google.com/apt cloud-sdk main" | tee -a /etc/apt/sources.list.d/google-cloud-sdk.list && \
    curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key --keyring /usr/share/keyrings/cloud.google.gpg  add - && \
    apt-get update -y && apt-get install -y google-cloud-sdk=357.0.0-0

RUN curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64-2.2.39.zip" -o "awscliv2.zip" && \
    unzip awscliv2.zip && \
    ./aws/install && \
    rm awscliv2.zip

RUN wget https://github.com/alexdobin/STAR/archive/2.7.6a.tar.gz && \
    tar -xzvf 2.7.6a.tar.gz && \
    rm 2.7.6a.tar.gz && \
    mkdir /software && \
    mv STAR-2.7.6a/ /software/STAR

RUN apt-get -qq -y remove curl gnupg wget curl python3-pip && \
    apt-get -qq -y autoremove && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /var/log/dpkg.log && \
    ln -s /usr/bin/python3 /usr/bin/python

ADD https://raw.githubusercontent.com/klarman-cell-observatory/cumulus/master/docker/monitor_script.sh /software
RUN chmod a+rx /software/monitor_script.sh

ENV PATH=/software:/software/STAR/bin/Linux_x86_64:$PATH
