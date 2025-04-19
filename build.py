import os
from pathlib import Path

# ==================================== SETTINGS ========================================

SRC_DIR = 'src'
BUILD_DIR = 'build'
LIB_DIR = 'lib'
DOCS_DIR = 'docs'

BUILD_RESOURCES_DIR = 'resources'
MUSIC_FILE = 'music.mp3'
REPLACEMENTS_FILE = 'replacements.sed'
FILES_FOR_ALT_FILE = 'files_for_alt.txt'
DIFF_CLASSES_FILE = 'classes.txt'

BUILD_SCRIPTS_DIR = 'scripts'
ALT_SCRIPT = 'alt.sh'
DIFF_SCRIPT = 'diff.sh'
HISTORY_SCRIPT = 'history.sh'
TEAM_SCRIPT = 'team.sh'

DEPLOY_DIR = '/home/timur1516/documents/dev/wildfly-35.0.1.Final/standalone/deployments'
RUN_SCRIPT = '/home/timur1516/documents/dev/wildfly-35.0.1.Final/bin/standalone.sh'

DB_CONFIG_FILE = '/home/timur1516/documents/dev/opi/lab3/web-lab-3/db.properties'

APP_NAME = 'web3'
BUILD_EXTENSION = 'war'

REMOTE_SERVER = 'helios'
REMOTE_SERVER_DIR = '~/'

LIBS_DICT = {
      'classmate-1.5.1.jar': 'https://repo1.maven.org/maven2/com/fasterxml/classmate/1.5.1/classmate-1.5.1.jar',
      'gson-2.10.1.jar': 'https://repo1.maven.org/maven2/com/google/code/gson/gson/2.10.1/gson-2.10.1.jar',
      'checker-qual-3.42.0.jar': 'https://repo1.maven.org/maven2/org/checkerframework/checker-qual/3.42.0/checker-qual-3.42.0.jar',
      'hibernate-commons-annotations-7.0.1.Final.jar': 'https://repo1.maven.org/maven2/org/hibernate/common/hibernate-commons-annotations/7.0.1.Final/hibernate-commons-annotations-7.0.1.Final.jar',
      'hibernate-core-6.6.1.Final.jar': 'https://repo1.maven.org/maven2/org/hibernate/orm/hibernate-core/6.6.1.Final/hibernate-core-6.6.1.Final.jar',        'istack-commons-runtime-4.1.1.jar': 'https://repo1.maven.org/maven2/com/sun/istack/istack-commons-runtime/4.1.1/istack-commons-runtime-4.1.1.jar',
      'jboss-logging-3.5.0.Final.jar': 'https://repo1.maven.org/maven2/org/jboss/logging/jboss-logging/3.5.0.Final/jboss-logging-3.5.0.Final.jar',
      'postgresql-42.7.4.jar': 'https://repo1.maven.org/maven2/org/postgresql/postgresql/42.7.4/postgresql-42.7.4.jar',
      'lombok-1.18.34.jar': 'https://repo1.maven.org/maven2/org/projectlombok/lombok/1.18.34/lombok-1.18.34.jar',
      'antlr4-runtime-4.13.0.jar': 'https://repo1.maven.org/maven2/org/antlr/antlr4-runtime/4.13.0/antlr4-runtime-4.13.0.jar',
      'junit-jupiter-api-5.10.2.jar': 'https://repo1.maven.org/maven2/org/junit/jupiter/junit-jupiter-api/5.10.2/junit-jupiter-api-5.10.2.jar',
      'junit-jupiter-engine-5.10.2.jar': 'https://repo1.maven.org/maven2/org/junit/jupiter/junit-jupiter-engine/5.10.2/junit-jupiter-engine-5.10.2.jar',
      'junit-platform-commons-1.10.2.jar': 'https://repo1.maven.org/maven2/org/junit/platform/junit-platform-commons/1.10.2/junit-platform-commons-1.10.2.jar',
      'junit-platform-console-standalone-1.10.2.jar': 'https://repo1.maven.org/maven2/org/junit/platform/junit-platform-console-standalone/1.10.2/junit-platform-console-standalone-1.10.2.jar',
      'junit-platform-engine-1.10.2.jar': 'https://repo1.maven.org/maven2/org/junit/platform/junit-platform-engine/1.10.2/junit-platform-engine-1.10.2.jar',
      'apiguardian-api-1.1.2.jar': 'https://repo1.maven.org/maven2/org/apiguardian/apiguardian-api/1.1.2/apiguardian-api-1.1.2.jar',
      'opentest4j-1.3.0.jar': 'https://repo1.maven.org/maven2/org/opentest4j/opentest4j/1.3.0/opentest4j-1.3.0.jar',
      'byte-buddy-1.14.18.jar': 'https://repo1.maven.org/maven2/net/bytebuddy/byte-buddy/1.14.18/byte-buddy-1.14.18.jar',
      'jakarta.activation-api-2.1.0.jar': 'https://repo1.maven.org/maven2/jakarta/activation/jakarta.activation-api/2.1.0/jakarta.activation-api-2.1.0.jar',
      'jakarta.inject-api-2.0.1.jar': 'https://repo1.maven.org/maven2/jakarta/inject/jakarta.inject-api/2.0.1/jakarta.inject-api-2.0.1.jar',
      'jakarta.persistence-api-3.1.0.jar': 'https://repo1.maven.org/maven2/jakarta/persistence/jakarta.persistence-api/3.1.0/jakarta.persistence-api-3.1.0.jar',
      'jakarta.transaction-api-2.0.1.jar': 'https://repo1.maven.org/maven2/jakarta/transaction/jakarta.transaction-api/2.0.1/jakarta.transaction-api-2.0.1.jar',
      'jakarta.xml.bind-api-4.0.0.jar': 'https://repo1.maven.org/maven2/jakarta/xml/bind/jakarta.xml.bind-api/4.0.0/jakarta.xml.bind-api-4.0.0.jar',
      'jakarta.jakartaee-web-api-9.0.0.jar': 'https://repo1.maven.org/maven2/jakarta/platform/jakarta.jakartaee-web-api/9.0.0/jakarta.jakartaee-web-api-9.0.0.jar',
      'jandex-3.2.0.jar': 'https://repo1.maven.org/maven2/io/smallrye/jandex/3.2.0/jandex-3.2.0.jar',
      'jaxb-core-4.0.2.jar': 'https://repo1.maven.org/maven2/org/glassfish/jaxb/jaxb-core/4.0.2/jaxb-core-4.0.2.jar',
      'jaxb-runtime-4.0.2.jar': 'https://repo1.maven.org/maven2/org/glassfish/jaxb/jaxb-runtime/4.0.2/jaxb-runtime-4.0.2.jar',
      'txw2-4.0.2.jar': 'https://repo1.maven.org/maven2/org/glassfish/jaxb/txw2/4.0.2/txw2-4.0.2.jar',
      'angus-activation-2.0.0.jar': 'https://repo1.maven.org/maven2/org/eclipse/angus/angus-activation/2.0.0/angus-activation-2.0.0.jar',
      'primefaces-14.0.0-jakarta.jar': 'https://repo1.maven.org/maven2/org/primefaces/primefaces/14.0.0/primefaces-14.0.0-jakarta.jar',
    }

if __name__ == '__main__':
    # Определяем пути к директориям
    src_dir = Path(SRC_DIR)
    lib_dir = Path(LIB_DIR)
    build_dir = Path(BUILD_DIR)
    resource_dir = Path(BUILD_RESOURCES_DIR)
    script_dir = Path(BUILD_SCRIPTS_DIR)
    deploy_dir = Path(DEPLOY_DIR)
    docs_dir = Path(DOCS_DIR)
    src_main_java_dir = src_dir / 'main' / 'java'
    src_test_java_dir = src_dir / 'test' / 'java'
    src_resources_dir = src_dir / 'main' / 'resources'
    src_webapp_dir = src_dir / 'main' / 'webapp'
    classes_dir = build_dir / 'classes'
    test_classes_dir = build_dir / 'test-classes'
    jar_dir = build_dir / APP_NAME
    native2ascii_dir = Path(src_resources_dir) / 'native2ascii'
    
    # Определяем пути к файлам
    jar_file = build_dir / f'{APP_NAME}.{BUILD_EXTENSION}'
    junit_jar_file = lib_dir / 'junit-platform-console-standalone-1.10.2.jar'
    manifest_file = jar_dir / 'META-INF' / 'MANIFEST.MF'

    replacements_file = resource_dir / REPLACEMENTS_FILE
    files_for_alt_file = resource_dir / FILES_FOR_ALT_FILE
    music_file = resource_dir / MUSIC_FILE
    diff_classes_file = resource_dir / DIFF_CLASSES_FILE

    history_diff_file = 'history_diff.txt'
    team_output_zip_file = 'revisions.zip'

    alt_script_file = script_dir / ALT_SCRIPT
    diff_script_file = script_dir / DIFF_SCRIPT
    history_script_file = script_dir / HISTORY_SCRIPT
    team_script_file = script_dir / TEAM_SCRIPT
    start_script_file = RUN_SCRIPT

    # Парсим файлы в директориях
    all_src_files = []
    for root, _, files in os.walk(src_dir):
        all_src_files.extend(Path(root) / f for f in files)

    java_files = []
    for root, _, files in os.walk(src_main_java_dir):
        java_files.extend(Path(root) / f for f in files if f.endswith('.java'))

    xml_files = []
    for root, _, files in os.walk(src_dir):
        xml_files.extend(Path(root) / f for f in files if f.endswith('.xml'))
    
    property_files = []
    for root, _, files in os.walk(src_resources_dir):
        property_files.extend(Path(root) / f for f in files if f.endswith('.properties'))

    test_java_files = []
    for root, _, files in os.walk(src_test_java_dir):
        test_java_files.extend(Path(root) / f for f in files if f.endswith('.java'))

    resource_files = []
    for root, _, files in os.walk(src_resources_dir):
        resource_files.extend((Path(root) / f).relative_to(src_resources_dir) for f in files if not f.endswith('.java'))

    webapp_files = []
    for root, _, files in os.walk(src_webapp_dir):
        webapp_files.extend((Path(root) / f).relative_to(src_webapp_dir) for f in files if not f.endswith('.java'))

    classpath = ':$\n'.join(f'{lib_dir / f}' for f in LIBS_DICT.keys())

    class_files = []
    for java_file in java_files:
        rel_path = java_file.relative_to(src_main_java_dir)
        class_file = classes_dir / rel_path.with_suffix('.class')
        class_files.append(class_file)
        if 'PointDTO.java' in str(java_file):
            class_files.append(classes_dir / rel_path.parent / 'PointDTO$$PointDTOBuilder.class')
    
    test_class_files = []
    for java_file in test_java_files:
        rel_path = java_file.relative_to(src_test_java_dir)
        test_class_file = test_classes_dir / rel_path.with_suffix('.class')
        test_class_files.append(test_class_file)

    ninja_content = f'''
# Правило для компиляции java файлов
rule javac
  command = mkdir -p $out_dir && javac -cp $classpath -d $out_dir $in
  description = Compiling Java source files
    
# Правило для создания jar/war файлов
rule war
  command = jar cf $out -C $in .
  description = Creating $out file
    
# Правило для копирования файлов
rule copy
  command = mkdir -p $$(dirname $out) && cp $in $out
  description = Copying $in to $out

# Правило для создания директорий
rule mkdir
    command = mkdir -p $out
    description = Creating directory $out

# Правило для создания создания текстового файла
rule write_manifest
    command = mkdir -p $$(dirname $out) && printf "Manifest-Version: 1.0\\nCreated-By: timur1516\\nBuilt-By: ninja\\n" > $out
    description = Creating file $out

# Правило для запуска тестов
rule run_tests
  command = java $junit_jar -jar $junitjar execute --class-path $classpath --scan-class-path
  description = Running tests

# Правило для удаления
rule rm
  command = rm -rf $file
  description = Removing $file

# Правило для валидации XML файла
rule validate_xml
  command = xmllint --noout $in
  description = Validating $in

# Правило для воспроизведения музыки
rule play_music
  command = mpg321 $music_file
  description = Playing music from $music_file

# Правило для выполнения native2ascii
rule native2ascii
  command = mkdir -p $$(dirname $out) && native2ascii -encoding ASCII $in $out
  description = Converting $in to ASCII

# Правило для генерации Javadoc
rule generate_javadoc
  command = mkdir -p $out && javadoc -classpath $classpath -d $out $in 2>/dev/null
  description = Generating Javadoc

# Правило для вычисления хеша и его записи в манифест
rule calculate_hash
  command = mkdir -p $$(dirname $manifest) && cat $in | $hasher | sed 's/ .*//' | xargs -I {{}} echo "$hasher: {{}}" >> $manifest
  description = Calculating $hasher

# Правило для отправки файла на сервер
rule send_to_server
  command = scp $in $remoteserver:$destdir
  description = Sending $in to $destdir on $remoteserver

# Правило для выполнения скрипта
rule execute_script
  command = $script $args
  description = Executing $script script

# Правило для загрузки библиотеки
rule load_lib
  command = mkdir -p $$(dirname $out) && cd $$(dirname $out) && curl -O -s $url
  description = Downloading $out from $url

# Правило для запуска программы
rule run_program
  command = java -cp $classpath:$out_dir $main_class
  description = Running $main_class

# Цели для загрузки библиотек
{'\n'.join(f'build {lib_dir / f}: load_lib\n  url = {LIBS_DICT[f]}' for f in LIBS_DICT.keys())}
build load_libs: phony {' $\n'.join(f'{lib_dir / f}' for f in LIBS_DICT.keys())}

# Цели для компиляции java файлов
build {' $\n'.join(str(f) for f in class_files)}: javac {' $\n'.join(str(f) for f in java_files)} | load_libs
  classpath = {classpath}
  out_dir = {classes_dir}
build compile_main: phony {' $\n'.join(str(f) for f in class_files)}

# Цель для компиляции тестов
build {' $\n'.join(str(f) for f in test_class_files)}: javac {' $\n'.join(str(f) for f in test_java_files)} | compile_main
  classpath = {classpath}:{classes_dir}
  out_dir = {test_classes_dir}
build compile_tests: phony {' $\n'.join(str(f) for f in test_class_files)}

# Цели для копирования ресурсов
{'\n'.join(f'build {classes_dir / f}: copy {src_resources_dir / f}' for f in resource_files)}
build copy_resources_to_classes: phony {' $\n'.join(str(classes_dir / f) for f in resource_files)}

build compile: phony compile_main copy_resources_to_classes

# Цели для копирования webapp
{'\n'.join(f'build {jar_dir / f}: copy {src_webapp_dir / f}' for f in webapp_files)}
build copy_webapp: phony {' $\n'.join(str(jar_dir / f) for f in webapp_files)}

# Цели для копирования библиотек
{'\n'.join(f'build {jar_dir / 'WEB-INF/lib' / f}: copy {lib_dir / f}' for f in LIBS_DICT.keys())}
build copy_libs: phony {' $\n'.join(str(jar_dir / 'WEB-INF/lib' / f) for f in LIBS_DICT.keys())}

# Цели для копирования классов
{'\n'.join(f'build {jar_dir / 'WEB-INF/classes' / f.relative_to(classes_dir)}: copy {f}' for f in class_files)}
build copy_classes: phony {' $\n'.join(str(jar_dir / 'WEB-INF/classes' / f.relative_to(classes_dir)) for f in class_files)}

# Цели для копирования ресурсов в war
{'\n'.join(f'build {jar_dir / 'WEB-INF/classes' / f}: copy {src_resources_dir / f}' for f in resource_files)}
build copy_resources_to_war: phony {' $\n'.join(str(jar_dir / 'WEB-INF/classes' / f) for f in resource_files)}

build copy_to_war: phony copy_webapp copy_libs copy_classes copy_resources_to_war

# Цели для создания MANIFEST.MF
build {manifest_file}: write_manifest
build manifest: phony {manifest_file}

# Цели для создания war файла
build {jar_dir}: mkdir
build {jar_file}: war {jar_dir} | copy_to_war manifest
build build: phony {jar_file}

# Цели для запуска тестов
build test: run_tests | compile_tests compile
  classpath = {lib_dir}:{classes_dir}:{test_classes_dir}
  junitjar = {junit_jar_file}

# Цели для очистки
build rm_build: rm
  file = {build_dir}
build rm_native2ascii: rm
  file = {native2ascii_dir}
build rm_docs: rm
  file = {docs_dir}
build rm_lib: rm
  file = {lib_dir}
build clean: phony rm_build rm_native2ascii rm_docs rm_lib

# Цели для валидации XML файлов
{'\n'.join(f'build validate_{f}: validate_xml {f}' for f in xml_files)}
build xml: phony {' $\n'.join(f'validate_{f}' for f in xml_files)}

# Цели для воспроизведения музыки
build music: play_music | build
  music_file = {music_file}

# Цели для native2ascii
{'\n'.join(f'build {native2ascii_dir / f.name}: native2ascii {f}' for f in property_files)}
build native2ascii: phony {' $\n'.join(f'{native2ascii_dir / f.name}' for f in property_files)}

# Цели для генерации Javadoc
build {docs_dir}: generate_javadoc {' $\n'.join(str(f) for f in java_files)} | load_libs
  classpath = {classpath}
build md5hash: calculate_hash {' $\n'.join(str(f) for f in all_src_files)} | {manifest_file}
  hasher = md5sum
  manifest = {manifest_file}
build sha1hash: calculate_hash {' $\n'.join(str(f) for f in all_src_files)} | {manifest_file}
  hasher = sha1sum
  manifest = {manifest_file}
build doc: phony {docs_dir} md5hash sha1hash

#Цели для отправки собранной программы на сервер
build scp: send_to_server {jar_file} | build
  remoteserver = {REMOTE_SERVER}
  destdir = {REMOTE_SERVER_DIR}

#Цели для выполнения alt
build alt: execute_script
  args = {replacements_file} {files_for_alt_file}
  script = {alt_script_file}

#Цели для выполнения diff
build diff: execute_script
  script = {diff_script_file}
  args = {diff_classes_file}

#Цели для выполнения history
build history: execute_script
  args = {history_diff_file}
  script = {history_script_file}

#Цели для выполнения team
build team: execute_script
  args = {jar_file} {team_output_zip_file}
  script = {team_script_file}

#Цели для выполнения env
build {deploy_dir / jar_file.name}: copy {jar_file}
build env: execute_script | {deploy_dir / jar_file.name}
  args = -DDB_CONFIG_PATH={DB_CONFIG_FILE}
  script = {start_script_file}
'''
    
    with open('build.ninja', 'w') as f:
        f.write(ninja_content)
    print('Generated build.ninja file')