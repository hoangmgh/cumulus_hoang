FROM debian:buster-slim
SHELL ["/bin/bash", "-c"]

RUN apt-get update && \
    apt-get install --no-install-recommends -y alien unzip build-essential dpkg-dev curl gnupg lsb-release procps python3 python3-pip && \
    export CLOUD_SDK_REPO="cloud-sdk-$(lsb_release -c -s)" && \
    echo "deb http://packages.cloud.google.com/apt $CLOUD_SDK_REPO main" | tee -a /etc/apt/sources.list.d/google-cloud-sdk.list && \
    curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key add - && \
    apt-get update && apt-get install -y google-cloud-sdk=374.0.0-0

RUN curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64-2.4.21.zip" -o "awscliv2.zip" && \
    unzip awscliv2.zip && \
    ./aws/install && \
    rm awscliv2.zip

RUN ln -s /usr/bin/python3 /usr/bin/python

RUN python -m pip install --upgrade pip --no-cache-dir && \
    python -m pip install pandas==1.3.5 --no-cache-dir && \
    python -m pip install packaging==21.3 --no-cache-dir && \
    python -m pip install stratocumulus==0.1.5 --no-cache-dir

RUN mkdir /software
ADD https://raw.githubusercontent.com/klarman-cell-observatory/cumulus/master/docker/monitor_script.sh /software
ADD cellranger-6.1.1.tar.gz /software

RUN apt-get -qq -y autoremove && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /var/log/dpkg.log

RUN chmod a+rx /software/monitor_script.sh
ENV PATH=/software:/software/cellranger-6.1.1:$PATH
ENV TMPDIR=/tmp
