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
    echo "                             default is ./ (current folder)."
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
    echo "          --tile-size:       tile size to use while rendering. If not set it's"
    echo "                             automatically determined, but this may result inefficient"
    echo "                             and increase the render times."
    echo "    -rf,  --resample-fac:    resample factor to interpolate data. By default it's not"
    echo "                             set and interpolation is disabled."
    echo "    -rx,  --res-x:           set the x resolution of the image."
    echo "    -ry,  --res-y:           set the y resolution of the image."
    echo "    -cr,  --color-ramp:      path of a color ramp JSON file to import."
    echo "    -fp,  --file-prefix      prefix to add before the file number. You can insert"
    echo "                             special characters to include the current date in the"
    echo "                             prefix using python standard formatting, for example"
    echo "                             %Y : four digits year"
    echo "                             %M : two digits month"
    echo "                             %d : two digits day"
    echo "                             the full list can be found here: strftime.org. You can"
    echo "                             also use these special characters (including brackets):"
    echo "                             {cb} : color by array name"
    echo "                             consider adding a character at the end (for example an"
    echo "                             underscore) to separate the prefix from the file number."
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
output_folder="./"
time_start=""
time_end=""
color_by=""
range_min=""
range_max=""
tile_size=""
resample_fac=""
res_x=""
res_y=""
color_ramp=""
file_prefix=""

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
            die "Error: '--output-folder' requires a non-empty option argument."
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
            die "Error: '--time-start' requires a non-empty option argument."
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
            die "Error: '--time-end' requires a non-empty option argument."
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
            die "Error: '--color-by' requires a non-empty option argument."
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
            die "Error: '--range-min' requires a non-empty option argument."
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
            die "Error: '--range-max' requires a non-empty option argument."
            ;;
        --tile-size)
              if [ "$2" ]; then
                  tile_size=$2
                  shift
              else
                  die "Error: '--tile-size' requires a non-empty option argument."
              fi
              ;;
        --tile-size=?*)
            tile_size=${1#*=}
            ;;
        --tile-size=)
            die "Error: '--tile-size' requires a non-empty option argument."
            ;;
        -rf|--resample-fac)
              if [ "$2" ]; then
                  resample_fac=$2
                  shift
              else
                  die "Error: '--resample-fac' requires a non-empty option argument."
              fi
              ;;
        -rf=?*|--resample-fac=?*)
            resample_fac=${1#*=}
            ;;
        -rf=|--resample-fac=)
            die "Error: '--resample-fac' requires a non-empty option argument."
            ;;
        -rx|--res-x)
              if [ "$2" ]; then
                  res_x=$2
                  shift
              else
                  die "Error: '--res-x' requires a non-empty option argument."
              fi
              ;;
        -rx=?*|--res-x=?*)
            res_x=${1#*=}
            ;;
        -rx=|--res-x=)
            die "Error: '--res-x' requires a non-empty option argument."
            ;;
        -ry|--res-y)
              if [ "$2" ]; then
                  res_y=$2
                  shift
              else
                  die "Error: '--res-y' requires a non-empty option argument."
              fi
              ;;
        -ry=?*|--res-y=?*)
            res_y=${1#*=}
            ;;
        -ry=|--res-y=)
            die "Error: '--res-y' requires a non-empty option argument."
            ;;
        -cr|--color-ramp)
              if [ "$2" ]; then
                  color_ramp=$2
                  shift
              else
                  die "Error: '--color-ramp' requires a non-empty option argument."
              fi
              ;;
        -cr=?*|--color-ramp=?*)
            color_ramp=${1#*=}
            ;;
        -cr=|--color-ramp=)
            die "Error: '--color-ramp' requires a non-empty option argument."
            ;;
        -fp|--file-prefix)
              if [ "$2" ]; then
                  file_prefix=$2
                  shift
              else
                  die "Error: '--file-prefix' requires a non-empty option argument."
              fi
              ;;
        -fp=?*|--file-prefix=?*)
            file_prefix=${1#*=}
            ;;
        -fp=|--file-prefix=)
            die "Error: '--file-prefix' requires a non-empty option argument."
            ;;

        *)
            break
    esac

    shift
done

echo ""
echo "Blender executable: $blender_ex"
echo "Input data: $input_data"
echo "Preset .blend: $preset"
echo ""

$blender_ex -b "$preset" -P "$F"/BVTK_render.py -- input_data:"$input_data" output_folder:"$output_folder" time_start:"$time_start" time_end:"$time_end" color_by:"$color_by" range_min:"$range_min" range_max:"$range_max" tile_size:"$tile_size" resample_fac:"$resample_fac" res_x:"$res_x" res_y:"$res_y" color_ramp:"$color_ramp" file_prefix:"$file_prefix"
