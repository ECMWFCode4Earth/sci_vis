#!/bin/bash

print_sintax () {
    echo ""
    echo "Usage: BVTK.sh input-data preset [options]"
    echo ""
    echo "    Required arguments"
    echo ""
    echo "    input_data:     path of the data file to visualize"
    echo "    preset:         path of the .blend preset file"
    echo ""
    echo "    Possible options"
    echo ""
    echo "    -o,   --output-folder:   path of the folder where the frame images will be stored,"
    echo "                             default is /tmp/"
    echo "    -ts,  --time-start:      index of the first time step to visualize, by default 0"
    echo "    -te,  --time-end:        index of the last time step to visualize, by default the"
    echo "                             last one available"
    echo "    -cb,  --color-by:        name of the array to use for coloring, if not specified"
    echo "                             one will be randomly picked among those available. You"
    echo "                             can initially type a random string and the script will"
    echo "                             show you the names of available arrays."
    echo "          --range-min:       lower value in the wanted range"
    echo "          --range-max:       higher value in the wanted range. If range_max and "
    echo "                             range_min are not given both, the range will be set to"
    echo "                             automatic."
    echo ""
}

# Bash script location
F=$(dirname $0)

# Import configuration
. $F/BVTK.config

if [ "$blender_ex" == "" ]
then
  echo ""
  echo "Please configure the path of the blender executable in the BVTK.config file."
  echo ""
  exit
fi

if (( $# < 2 ))
then
    echo "Bad number of arguments $#, expecting at least 2"
    print_sintax
    exit
fi

# Required arguments
input_data=$1
preset=$2

shift 2

# Options
output_folder="/tmp/"
time_start=""
time_end=""
color_by=""
range_min=""
range_max=""

while :; do
    case $1 in
        -h|-\?|--help)
            print_sintax
            exit
            ;;
        -o|--output-folder)
              if [ "$2" ]; then
                  output_folder=$2
                  shift
              else
                  die "Error: '--output-folder' requires a non-empty option argument."
              fi
              ;;
        -o=?*|--output-folder=?*)
            output_folder=${1#*=}
            ;;
        -o=|--output-folder=)
            die "Error: '--output_folder' requires a non-empty option argument."
            ;;
        -ts|--time-start)
              if [ "$2" ]; then
                  time_start=$2
                  shift
              else
                  die "Error: '--time-start' requires a non-empty option argument."
              fi
              ;;
        -ts=?*|--time-start=?*)
            time_start=${1#*=}
            ;;
        -ts=|--time-start=)
            die "Error: '--output_folder' requires a non-empty option argument."
            ;;
        -te|--time-end)
              if [ "$2" ]; then
                  time_end=$2
                  shift
              else
                  die "Error: '--time-end' requires a non-empty option argument."
              fi
              ;;
        -te=?*|--time-end=?*)
            time_end=${1#*=}
            ;;
        -te=|--time-end=)
            die "Error: '--output_folder' requires a non-empty option argument."
            ;;
        -cb|--color-by)
              if [ "$2" ]; then
                  color_by=$2
                  shift
              else
                  die "Error: '--color-by' requires a non-empty option argument."
              fi
              ;;
        -cb=?*|--color-by=?*)
            color_by=${1#*=}
            ;;
        -cb=|--color-by=)
            die "Error: '--output_folder' requires a non-empty option argument."
            ;;
        --range-min)
              if [ "$2" ]; then
                  range_min=$2
                  shift
              else
                  die "Error: '--range-min' requires a non-empty option argument."
              fi
              ;;
        --range-min=?*)
            range_min=${1#*=}
            ;;
        --range-min=)
            die "Error: '--output_folder' requires a non-empty option argument."
            ;;
        --range-max)
              if [ "$2" ]; then
                  range_max=$2
                  shift
              else
                  die "Error: '--range-max' requires a non-empty option argument."
              fi
              ;;
        --range-max=?*)
            range_max=${1#*=}
            ;;
        --range-max=)
            die "Error: '--output_folder' requires a non-empty option argument."
            ;;
        *)
            break
    esac

    shift
done


echo "Blender executable: $blender_ex"
echo "Input data:         $input_data"
echo "Preset .blend:      $preset"

# -b : lancia blender in background
# -P : esegui questo script
# -- : passa il testo di seguito allo script python
 
$blender_ex -b $preset -P $F/render.py -- input_data:$input_data output_folder:$output_folder time_start:$time_start time_end:$time_end color_by:$color_by range_min:$range_min range_max:$range_max
