RUNTIME=python3.8

SELENIUM_VER=3.141.0
CHROME_BINARY_VER=v1.0.0-57 # based on Chromium 69.0.3497.81
CHROMEDRIVER_VER=86.0.4240.22       # supports Chrome v69-71

OUT_DIR=/out/build/chrome_headless/python/lib/$RUNTIME/site-packages

docker run -v $(pwd):/out -it lambci/lambda:build-$RUNTIME \
    pip install selenium==$SELENIUM_VER -t $OUT_DIR

pushd build/chrome_headless

DRIVER_URL=https://chromedriver.storage.googleapis.com/$CHROMEDRIVER_VER/chromedriver_linux64.zip
curl -SL $DRIVER_URL >chromedriver.zip
unzip chromedriver.zip
rm chromedriver.zip

# download chrome binary
CHROME_URL=https://github.com/adieuadieu/serverless-chrome/releases/download/$CHROME_BINARY_VER/stable-headless-chromium-amazonlinux-2.zip
curl -SL $CHROME_URL >headless-chromium.zip
unzip headless-chromium.zip
rm headless-chromium.zip

cp ../../lambda_function.py build/chrome_headless/
cp ../../cat.py build/chrome_headless/

zip -r ../../chrome_headless_3_9.zip *
