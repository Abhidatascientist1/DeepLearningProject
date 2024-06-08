from setuptools import find_packages,setup

def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements =file_obj.readlines()
        requirements=[require.replace("\n,"") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements



setup(

name = "Xray",
version = "0.0.1",
author = "Abhishek Barve",
author_email = "Abhifun.643@gmail.com",
install_requires=get_requirements(),
package =find_packages()


)