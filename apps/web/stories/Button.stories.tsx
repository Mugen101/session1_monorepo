import type { Meta, StoryObj } from '@storybook/react';
import { Button } from '../components/ui/Button';
import React, { useState } from 'react';

const meta: Meta<typeof Button> = {
  title: 'Design System/Button',
  component: Button,
  parameters: {
    a11y: {
      // accessibility config
    },
  },
};
export default meta;

type Story = StoryObj<typeof Button>;

export const Default: Story = {
  args: {
    children: 'Button',
  },
};

export const Interaction: Story = {
  render: (args) => {
    const [pressed, setPressed] = useState(false);
    return (
      <Button {...args} onClick={() => setPressed((p) => !p)}>
        {pressed ? 'Pressed' : 'Press Me'}
      </Button>
    );
  },
};
