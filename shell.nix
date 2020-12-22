with import <nixpkgs> {};
mkShell {
   buildInputs = [
      (python3.withPackages (ps: with ps; [
         pytest
         pytest-watch
         pytestcov
         black
         pip
      ]))
   ];

  shellHook = ''
     export PIP_PREFIX="$(pwd)/.build/pip_packages"
     export PATH="$PIP_PREFIX/bin:$PATH"
     export PYTHONPATH="$PIP_PREFIX/${python3.sitePackages}:$PYTHONPATH"
     export PYTHONDONTWRITEBYTECODE=x
     unset SOURCE_DATE_EPOCH
  '';
}
