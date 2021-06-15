#!/usr/bin/env bash

# Source the common helpers script.
source scripts/common.bash


# Check if we're in a virtual environment
pip_opt_user=""
if [ -z ${VIRTUAL_ENV} ]; then
    # if not in virtual environment
    pip_opt_user="--user"
fi


execute_command_checked "./exec-reqs-install.sh"

# add -s for verbose output

printf "${yellow}"
print_banner "Python 3"
printf "${normal}\n"

find . -name "__pycache__" -exec rm -rf {} \; >& /dev/null
find . -name "*.py?" -exec rm {} \;           >& /dev/null

#if [ -e tests ]; then
#    rm -rf tests
#fi

options=(
    --cov=setprogramoptions
    --cov-report=term
    --cov-report=term-missing
    --cov-report=html
    --cov-report=xml
    --cov-config=.coveragerc
    )

python3 -m pytest ${options[@]}
err=$?


# Install the package
execute_command_checked "python3 -m pip wheel --no-deps -w dist . >& _test-build-dist.log"
execute_command_checked "python3 -m pip install ${pip_opt_user} . >& _test-install.log"


# Check the examples
execute_command_checked "pushd examples"
execute_command_checked "python3 example-01.py >& _test-example-01.log"
execute_command_checked "python3 example-02.py >& _test-example-02.log"
execute_command_checked "python3 example-03.py >& _test-example-03.log"
execute_command_checked "popd"


# Clean up installed package
execute_command_checked "python3 -m pip uninstall -y setprogramoptions >& _test-uninstall.log"


# Clean up generated bytecode
if [ $err -eq 0 ]; then
    execute_command "find . -name '__pycache__' -exec rm -rf {} \;          > /dev/null 2>&1"
    execute_command "find . -name '*.py?' -exec rm {} \;                    > /dev/null 2>&1"
    execute_command "find . -depth 2 -name '_example-*.ini' -exec rm {} \;  > /dev/null 2>&1"
    execute_command "find . -maxdepth 2 -name '_test-*.log' -exec rm {} \;  > /dev/null 2>&1"
    execute_command "find . -maxdepth 1 -name '___*.ini' -exec rm {} \;     > /dev/null 2>&1"
fi


echo -e ""
if [ $err != 0 ]; then
    printf "${red}"
    print_banner "TESTING FAILED"
    printf "${normal}"
else
    printf "${green}"
    print_banner "TESTING PASSED"
    printf "${normal}"
fi
echo -e ""


exit $err
